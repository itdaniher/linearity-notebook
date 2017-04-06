from laplace import *

x = sympy.Function('X')
t = sympy.var('t')
dxdt = x(t).diff(t,t)
d2xdt = dxdt.diff(t,t)
d3xdt = d2xdt.diff(t,t)
expression = sympy.Eq(d2xdt + 3*dxdt+4*x(t), e**(j*t))
sympy.dsolve(expression, x(t))
### Eq(X(t), (C1*sin(sqrt(7)*t/2) + C2*cos(sqrt(7)*t/2))/sqrt(exp(t)) + (C3*sin(sqrt(7)*t/2) + C4*cos(sqrt(7)*t/2))*sqrt(exp(t)) + 0.5*exp(1.0*I*t))
sympy.laplace_transform(d2xdt + 3*dxdt+4*x(t), t, s)
### 4*LaplaceTransform(X(t), t, s) + 3*LaplaceTransform(Derivative(X(t), t, t), t, s) + LaplaceTransform(Derivative(X(t), t, t, t, t), t, s)
sympy.laplace_transform(e**(j*t), t, s)
### (1.0/(s - I), 0, True)

drawBode(1/(s**3+3*s**2+2*s+12))

filt = sys2e(signal.lti(*signal.butter(1, (2,20), 'bandpass', True, 'ba')))
drawBode(filt)
