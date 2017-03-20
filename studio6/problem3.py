import numpy as np

Arr = lambda txt: np.array([[eval(x.strip()) for x in y.split() if x.strip() != ''] for y in txt.split(';') if y.split() != ''])

A = (1/3)*Arr('2 1 -2; 2 -2 1; 1 2 2')
print('A', A)
print('inverse A', np.linalg.inv(A))

B = (1/5)*Arr('0 0 3 4; 0 0 -4 3; 4 3 0 0; 4 -3 0 0')
print('B', B)
print('inverse B', np.linalg.inv(B))

print("the inverse of a matrix is equal to the transposition of the mutually orthogonal vectors that when dotted with a vector of constants is equal to.... ugh.")

ANSWERS = """
A [[ 0.66666667  0.33333333 -0.66666667]
 [ 0.66666667 -0.66666667  0.33333333]
 [ 0.33333333  0.66666667  0.66666667]]
inverse A [[ 0.66666667  0.66666667  0.33333333]
 [ 0.33333333 -0.66666667  0.66666667]
 [-0.66666667  0.33333333  0.66666667]]
B [[ 0.   0.   0.6  0.8]
 [ 0.   0.  -0.8  0.6]
 [ 0.8  0.6  0.   0. ]
 [ 0.8 -0.6  0.   0. ]]
inverse B [[ 0.          0.          0.625       0.625     ]
 [ 0.          0.          0.83333333 -0.83333333]
 [ 0.6        -0.8         0.          0.        ]
 [ 0.8         0.6         0.          0.        ]]
the inverse of a matrix is equal to the transposition of the mutually orthogonal vectors that when dotted with a vector of constants is equal to.... ugh.
"""
