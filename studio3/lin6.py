### current bpython session - make changes and save to reevaluate session.
### lines beginning with ### will be ignored.
### To return to bpython without reevaluating make no changes to this file
### or save an empty file.
import numpy as np
arrayer = lambda txt: np.array([[float(x.strip()) for x in y.split() if x.strip() != ''] for y in txt
### .split(';')])
adjacency_matrix = arrayer('0 1 1 1 1; 1 0 1 0 0; 0 1 0 1 0; 0 0 0 0 1; 0 0 0 1 0')
adjacency_matrix
### array([[ 0.,  1.,  1.,  1.,  1.],
###        [ 1.,  0.,  1.,  0.,  0.],
###        [ 0.,  1.,  0.,  1.,  0.],
###        [ 0.,  0.,  0.,  0.,  1.],
###        [ 0.,  0.,  0.,  1.,  0.]])
adjacency_matrix.T
### array([[ 0.,  1.,  0.,  0.,  0.],
###        [ 1.,  0.,  1.,  0.,  0.],
###        [ 1.,  1.,  0.,  0.,  0.],
###        [ 1.,  0.,  1.,  0.,  1.],
###        [ 1.,  0.,  0.,  1.,  0.]])
adjacency_matrix.shape
### (5, 5)
for row in range(adjacency_matrix.shape[0]):
    adjacency_matrix[row] /= np.sum(adjacency_matrix[row])

adjacency_matrix
### array([[ 0.  ,  0.25,  0.25,  0.25,  0.25],
###        [ 0.5 ,  0.  ,  0.5 ,  0.  ,  0.  ],
###        [ 0.  ,  0.5 ,  0.  ,  0.5 ,  0.  ],
###        [ 0.  ,  0.  ,  0.  ,  0.  ,  1.  ],
###        [ 0.  ,  0.  ,  0.  ,  1.  ,  0.  ]])
difference_matrix = adjacency_matrix.T
### array([[ 0.  ,  0.5 ,  0.  ,  0.  ,  0.  ],
###        [ 0.25,  0.  ,  0.5 ,  0.  ,  0.  ],
###        [ 0.25,  0.5 ,  0.  ,  0.  ,  0.  ],
###        [ 0.25,  0.  ,  0.5 ,  0.  ,  1.  ],
###        [ 0.25,  0.  ,  0.  ,  1.  ,  0.  ]])
np.linalg.eig(difference_matrix)
### (array([ 1.       ,  0.6830127, -0.1830127, -1.       , -0.5      ]), 
### array([[ -7.21644966e-16,   2.91376821e-01,   8.67456484e-01,
###          -6.81335581e-17,   6.32455532e-01],
###        [ -8.84708973e-16,   3.98028139e-01,  -3.17511110e-01,
###           2.45280809e-16,  -6.32455532e-01],
###        [ -7.28583860e-16,   3.98028139e-01,  -3.17511110e-01,
###           0.00000000e+00,   3.16227766e-01],
###        [  7.07106781e-01,  -4.84592198e-01,  -2.13376265e-01,
###           7.07106781e-01,   9.41387621e-17],
###        [  7.07106781e-01,  -6.02840901e-01,  -1.90579993e-02,
###          -7.07106781e-01,  -3.16227766e-01]]))
### 

# NB the magnitude of the last two eigenvectors are significantly larger than that of the others, indicating the significance of their attraction
