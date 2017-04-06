import sympy

import matplotlib
matplotlib.use('cairo')

from matplotlib import pyplot
import mpmath
import numpy as np
import scipy.signal as signal

j = sympy.I
e = sympy.exp(1)
s = sympy.var('s')

ct = 100

mpmath.mp.dps = 40;
mpmath.mp.pretty = True

blacks = lambda G_s, H_s: G_s/(1+G_s*H_s)

def eeval(expression, w):
    """ evaluate a sympy expression at omega. return magnitude, phase."""
    num, den = e2nd(expression)
    y = np.polyval(num, 1j*w) / np.polyval(den, 1j*w)
    phase = np.arctan2(y.imag, y.real) * 180.0 / np.pi
    mag = abs(y)
    return mag, phase

def bode(expression, n = 10):
    """ evaluate an expression at N points, returning frequency, magnitude, and phase """
    decibels = lambda lin: 20*np.log10(np.abs(lin))
    num, den = e2nd(expression)
    freqs = signal.findfreqs(num, den, n)
    magnitude = np.array([])
    phase = np.array([])
    for freq in freqs:
        (m, p) = eeval(expression, freq)
        magnitude = np.append(magnitude, m)
        if p >= 0:
            p = -360+p
        phase = np.append(phase, p)
    magnitude = np.array([decibels(x) for x in magnitude])
    return freqs, magnitude, phase

def e2nd(expression):
    """ basic helper function that accepts a sympy expression, expands it, 
    attempts to simplify it, and returns a numerator and denomenator pair for the instantiation of a scipy LTI system object. """
    expression = expression.expand().cancel()
    n = sympy.Poly(sympy.numer(expression), s).all_coeffs()
    d = sympy.Poly(sympy.denom(expression), s).all_coeffs()
    return ([float(x) for x in n], [float(x) for x in d])

def pade(t, n):
    """ pade approximation of a time delay, as per mathworks' controls toolkit.
    supports arbitrary precision mathematics via mpmath and sympy"
    for more information, see:
        * http://home.hit.no/~hansha/documents/control/theory/pade_approximation.pdf 
        * http://www.mathworks.com/help/control/ref/pade.html
    """
    # e**(s*t) -> laplace transform of a time delay with 't' duration
    # e**x -> taylor series
    taylor = mpmath.taylor(sympy.exp, 0, n*2)
    (num, den) = mpmath.pade(taylor, n, n)
    num = sum([x*(-t*s)**y for y,x in enumerate(num[::-1])])
    den = sum([x*(-t*s)**y for y,x in enumerate(den[::-1])])
    return num/den

def sys2e(system):
    """ basic helper function that accepts an instance of the scipy.signal.lti class
    and returns a sympy expression given by the ratio of the expanded numerator and denomenator"""
    den = sum([x*s**y for y,x in enumerate(system.den[::-1])])
    num = sum([x*s**y for y,x in enumerate(system.num[::-1])])
    return sympy.factor(num/den)

def findZero(arr):
    return np.argmin(np.abs(arr))

def phaseMargin(expression):
    w, mag, phase = bode(expression, n=ct)
    crossingPoint = findZero(mag) # point where magnitude is closest to 0dB
    return {"w_c": w[crossingPoint], "p_m": phase[crossingPoint]+180}

def gainMargin(expression):
    w, mag, phase = bode(expression, n=ct)
    unstablePoint = findZero(-phase-180)
    return {"w": w[unstablePoint], "g_m": -mag[unstablePoint]}

def steadyStateError(expression):
    """ use sympy to determine limit at 0. """
    errors = {}
    for order, name in enumerate(['dc', 'step', 'ramp', 'parabola']):
        errors[name] = 1/(1+sympy.limit(s*expression*1/s**order, s, 0))
    return errors #{"sse": 1/(1+fvt)}

def reducedGainCompensate(expression, target):
    """ find the uncompensated system's magnitude at the right phase to give the right margin, normalize against it"""
    w, mag, phase = bode(expression, n=ct)
    phaseTarget = (-180 + target)
    targetIndex = findZero(phaseTarget - phase)
    magnitude = mag[targetIndex]
    magnitude = 10**(magnitude/20)
    return {"K": 1/magnitude}, 1/magnitude

def dominatePoleCompensate(expression, target):
    """ add a pole, call reducedGainCompensate"""
    K = reducedGainCompensate(1/s*expression, target)[0]['K']
    return {"K": K}, K/s

def lagCompensate(expression, target):
    w, mag, phase = bode(expression, n=ct)
    phaseTarget = -180 + (target + 6) # find location of new crossing goal; extra '-6' is from 10/wc rule
    targetIndex = findZero(phaseTarget - phase)
    w_c = w[targetIndex]
    tau = 10/w_c
    # equation for basic lag compensator
    alpha = eeval(expression, w_c)[0]
    G_c = (tau*s+1)/(alpha*tau*s+1)
    return {"alpha": alpha, "tau": tau}, G_c

def leadCompensate(expression, target):
    # alpha = 10 for 55 degrees phase margin
    w, mag, phase = bode(expression, n=ct)
    alpha = 10
    phaseTarget = -(180 + (55 - target))
    targetIndex = findZero(phase-phaseTarget)
    w_c = w[targetIndex]
    tau = 1 / (np.sqrt(alpha) * w_c)
    G_c = (alpha*tau*s+1)/(tau*s+1)
    # get magnitude of loop transfer function L(s) at w_c
    K_l = 1/ eeval(G_c*expression, w_c)[0] 
    # equation for basic lead compensator
    G_c = K_l * (alpha*tau*s+1)/(tau*s+1)
    return {"K_l": K_l, "alpha": alpha, "tau":tau}, G_c

def drawBode(expression, f1=pyplot.figure(), color="k", labeled=""):
    """ draw bode plot for a given scipy.signal.lti instance. """
    pyplot.clf()
    adjustprops = dict(left=0.1, bottom=0.1, right=0.97, top=0.93, hspace=0.2)
    f1.subplots_adjust(**adjustprops)
    f1.suptitle(str(expression))
    magPlot = f1.add_subplot(2, 1, 1)
    phasePlot = f1.add_subplot(2, 1, 2, sharex=magPlot)
    w, mag, phase = bode(expression, n=ct)
    magPlot.semilogx(w, mag, label=labeled, color=color)
    magPlot.set_title("magnitude")
    magPlot.set_ylabel("amplitude (dB)")
    phasePlot.semilogx(w, phase, label=labeled, color=color)
    phasePlot.set_title("phase")
    phasePlot.set_xlabel("radians per second")
    phasePlot.set_ylabel("degrees")
    pyplot.setp(magPlot.get_xticklabels(), visible=False)
    pyplot.legend(loc="best")
    unambiguous_printable_name = sympy.srepr(expression).replace(', prec=15', '')
    f1.savefig("./"+unambiguous_printable_name+".png", dpi = 300)
    return f1

if __name__ == "__main__":
    H_s = -10/((s+1)*(0.1*s+1)*(0.01*s+1))
    drawBode(H_s)
