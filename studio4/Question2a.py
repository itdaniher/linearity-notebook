from lin1 import *
D = Arr('0.9 0 ; 0 0.1')

ANSWERS_2a = """
operates by shrinking by 9/10ths and 1/10th at right angles to eachother, as the non-zero values lie along the diagonal

there're two axes at play, so two linearly independent eigenvectors, each with their unique eigenvalues.

as we have zeros where our values don't lie along the identity matrix, (basis = I?), it's pretty easy to read the values directly off the matrix

A*v=l*v
A*v-l*v=0
A*v-l*I*v=0
(A-l*I)*v=0

only sensible when l != 0

scalar multiplication of l across the identity matrix

elementwise subtraction of l*I from the original matrix

for a matrix 'a b; c d', it's pretty easy to see how

'a-l b; c d-l'

becomes:

l**2-(a+d)l+(ad-bc)=0


for our specific case:

'0.9-l 0; 0 0.1-l' = '0 0; 0 0' 

(just noticed why we multiply by I here)

and the only values for our eigenvalues here are the values along our diagonal!

we can check our math with the expansion provided

(l**2-(0.9+1.0)*l+(0.9*0.1-0*0) = 0

x**2 - x + 0.09 = 0

gives x=0.9,0.1

makes perfect sense!
"""


eigen_vs(D)
### (array([ 0.9,  0.1]), array([[ 1.,  0.],
###        [ 0.,  1.]]))
###


# Our answers were correct!

