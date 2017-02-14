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
###   File "/usr/lib/python2.7/dist-packages/numpy/linalg/linalg.py", line 384, in solve
###     r = gufunc(a, b, signature=signature, extobj=extobj)
###   File "/usr/lib/python2.7/dist-packages/numpy/linalg/linalg.py", line 90, in _raise_linalgerror_singular
###     raise LinAlgError("Singular matrix")
### LinAlgError: Singular matrix
solve(V[2:6].T, [1]*4)
### array([ 1., -1.,  2., -1.])
solve(Arr('2 1 4 0; 0 0 2 0; 0 0 0 1; 1 2 1 2').T, [1]*4)
### array([ 0.33333333, -0.33333333,  0.33333333,  0.33333333])

"""
ANSWERS 

i) no valid bases specified as none constrain in the appropriate number of dimensions (4)
ii) Only the first combination, as discussed below, is a valid span
iii)

so, looking for compatible combinations of vectors V1..6, I visually identified V1..4, V3..6, and a matrix comprised of {V1, V4, V5, V6}

skipped the step of solving for the homogenous solution here, and then using the homogenous solution and the specified points
provide the directly extracted the particular solutions Cp for all As
besides the provided [1/4, -3/4, 1, -1/2], we also found [1, -1, 2, -1] and [1/3, -1/3, 1/3, 1/3]

iv) TBD
"""
