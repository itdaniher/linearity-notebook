A = s.Matrix(2,2,get_unique(4))
B = s.Matrix(2,2,get_unique(4))
(A*B).det()
### i*l*m*p - i*l*n*o - j*k*m*p + j*k*n*o
A.det()
### i*l - j*k
B.det()
### m*p - n*o
(A*B).det() == s.expand(A.det()*B.det())
### True
diagonal_test = s.diag(*get_unique(3))
n2 = s.Matrix(2,2,get_unique(4))
n2.eigenvals().values()
### [1, 1]
n2.eigenvals().keys()
### [u/2 + x/2 - sqrt(u**2 - 2*u*x + 4*v*w + x**2)/2, u/2 + x/2 + sqrt(u**2 - 2*u*x + 4*v*w + x**2)/2]
n2.eigenvals().keys()[0]*n2.eigenvals().keys()[1]
### (u/2 + x/2 - sqrt(u**2 - 2*u*x + 4*v*w + x**2)/2)*(u/2 + x/2 + sqrt(u**2 - 2*u*x + 4*v*w + x**2)/2)
s.simplify(_)
### u*x - v*w
n2.eigenvals().keys()
### [u/2 + x/2 - sqrt(u**2 - 2*u*x + 4*v*w + x**2)/2, u/2 + x/2 + sqrt(u**2 - 2*u*x + 4*v*w + x**2)/2]
n3 = s.diag(a,d,e)
n3[3] = c
n3[1] = b
n3
### Matrix([
### [a, b, 0],
### [c, d, 0],
### [0, 0, e]])
n3.charpoly()
### PurePoly(_lambda**3 + (-a - d - e)*_lambda**2 + (a*d + a*e - b*c + d*e)*_lambda - a*d*e + b*c*e, _lambda, domain='ZZ[a,b,c,d,e]')
n2.charpoly()
### PurePoly(_lambda**2 + (-u - x)*_lambda + u*x - v*w, _lambda, domain='ZZ[x,u,v,w]')
n2
### Matrix([
### [u, v],
### [w, x]])
c4 = s.Matrix(3, 3, (a, b, c, 0, 1, 0, 0, 0, 1))
### Matrix([
### [a, b, c],
### [0, 1, 0],
### [0, 0, 1]])
c4.charpoly()
### PurePoly(_lambda**3 + (-a - 2)*_lambda**2 + (2*a + 1)*_lambda - a, _lambda, domain='ZZ[a]')
### 
