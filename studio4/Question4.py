### current bpython session - make changes and save to reevaluate session.
### lines beginning with ### will be ignored.
### To return to bpython without reevaluating make no changes to this file
### or save an empty file.
import sympy as s
import string

# l is lambda, or our eigenvalues
l = s.var('l')
def get_unique(N_vars, sets = string.lowercase):
    symbol_names = []
    while len(symbol_names) < N_vars:
        for letter in sets:
            if letter not in globals().keys() and letter not in symbol_names:
                symbol_names += [letter]
                break
        if letter == sets[-1]:
            break
    return s.var(' '.join(symbol_names))

A = s.Matrix(2,2,get_unique(4))
B = s.Matrix(2,2,get_unique(4))
A
### Matrix([
### [a, b],
### [c, d]])
B
### Matrix([
### [e, f],
### [g, h]])
(A*B).det()
### a*d*e*h - a*d*f*g - b*c*e*h + b*c*f*g
A.det()
### a*d - b*c
B.det()
### e*h - f*g
(A*B).det() == s.expand(A.det()*B.det())
### True
diagonal_test = s.diag(*get_unique(3))
n2 = s.Matrix(2,2,(a, b, c, d))
n2
### Matrix([
### [a, b],
### [c, d]])
s.solveset(n2.charpoly(l).as_expr(), l) 
### {a/2 + d/2 - sqrt(a**2 - 2*a*d + 4*b*c + d**2)/2, a/2 + d/2 + sqrt(a**2 - 2*a*d + 4*b*c + d**2)/2}
n2.eigenvals().keys()
### [a/2 + d/2 - sqrt(a**2 - 2*a*d + 4*b*c + d**2)/2, a/2 + d/2 + sqrt(a**2 - 2*a*d + 4*b*c + d**2)/2]
s.solveset(l**2-(a+d)*l+(a*d-b*c), l)
### {a/2 + d/2 - sqrt(a**2 - 2*a*d + 4*b*c + d**2)/2, a/2 + d/2 + sqrt(a**2 - 2*a*d + 4*b*c + d**2)/2}

ANSWER_4a = """

above, we can see that the eigenvalues are equivalent to the roots of the characteristic polynomial, which are equal to the roots of the provided formulation for lambda

"""


n3 = s.diag(a,d,e)
n3[3] = c
n3[1] = b
n3
### Matrix([
### [a, b, 0],
### [c, d, 0],
### [0, 0, e]])
n3.charpoly(l).as_expr()
### -a*d*e + b*c*e + l**3 + l**2*(-a - d - e) + l*(a*d + a*e - b*c + d*e)
n2.charpoly(l).as_expr()
### a*d - b*c + l**2 + l*(-a - d)
c4 = s.Matrix(3, 3, (a, b, c, 0, 1, 0, 0, 0, 1))
c4.charpoly(l).as_expr(l)
### -a + l**3 + l**2*(-a - 2) + l*(2*a + 1)

ANSWER_4bc = """

see above

"""
