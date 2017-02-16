# import trainingwheels
from lin1 import *

# Question 1 Part A


V = Arr('2 1 4 0; 2 3 4 0; 2 3 4 1; 0 0 2 0; 0 0 0 1; 1 2 1 2')
# accessing "T" returns the transposed matrix
V.T
### array([[ 2.,  2.,  2.,  0.,  0.,  1.],
###        [ 1.,  3.,  3.,  0.,  0.,  2.],
###        [ 4.,  4.,  4.,  2.,  0.,  1.],
###        [ 0.,  0.,  1.,  0.,  1.,  2.]])

# solve our homogenous solution for the validated trivial case
solve(V[0:4].T, [0]*4)
### array([ 0.,  0.,  0.,  0.])
# oh look, it's all zeros

solve(V[0:4].T, [1]*4)
### array([ 0.25, -0.75,  1.  , -0.5 ])
# messing around, this one didn't work, for visually apparent reasons
solve(V[1:5].T, [1]*4)
### Traceback (most recent call last):
###   File "<input>", line 1, in <module>
###     solve(V[1:5].T, [1]*4)
###   File "lin1.py", line 46, in <lambda>
###     solve = lambda A, b: np.linalg.solve(A, b)
### LinAlgError: Singular matrix
solve(V[2:6].T, [1]*4)
### array([ 1., -1.,  2., -1.])
solve(Arr('2 1 4 0; 0 0 2 0; 0 0 0 1; 1 2 1 2').T, [1]*4)
### array([ 0.33333333, -0.33333333,  0.33333333,  0.33333333])

solve(Arr('2 1 4 0; 2 3 4 0; 0 0 2 0; 0 0 0 1').T, [0]*4)
### array([ 0.,  0.,  0.,  0.])

"""
ANSWERS 

i) no valid bases specified as none constrain in the appropriate number of dimensions (4)
ii) Only the first combination, as discussed below, is a valid span
iii)

so, looking for compatible combinations of vectors V1..6, I visually identified V1..4, V3..6, and a m

I skipped the step of solving for the homogenous solution here, using my formulated matrix and an alg
    provide the directly extracted the particular solutions Cp for all relevant As

besides the provided [1/4, -3/4, 1, -1/2], we also found [1, -1, 2, -1] and [1/3, -1/3, 1/3, 1/3]

iv) we're looking for the set of points where the system of equations specified by V1, V2, V3, and V4 intersect - the combination of values for a vector 'a b c d' that's dotted with our matrix A to satisfy the conditions A*v=0 - the only set of values the solver found for v were [0, 0, 0, 0]
"""
