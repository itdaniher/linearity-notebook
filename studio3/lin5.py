#### Problem number 5, diving right in!

D = arrayer('2 0; 0 0.5')
R = lambda theta: np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
matrix_product = lambda theta: np.dot(R(-theta), np.dot(D, R(theta)))
eigs_product = lambda theta: np.linalg.eig(matrix_product(theta))
# let's take this thing for a spin!
eigs_product(np.pi/2)
### (array([ 0.5,  2. ]), array([[  1.00000000e+00,  -6.12323400e-17],
###        [  0.00000000e+00,   1.00000000e+00]]))
eigs_product(0)
### (array([ 2. ,  0.5]), array([[ 1.,  0.],
###        [ 0.,  1.]]))
eigs_product(0.1)
### (array([ 2. ,  0.5]), array([[ 0.99500417,  0.09983342],
###        [-0.09983342,  0.99500417]]))
eigs_product(0.11)
### (array([ 2. ,  0.5]), array([[ 0.9939561,  0.1097783],
###        [-0.1097783,  0.9939561]]))
matrix_product(0.1)
### array([[ 1.98504993, -0.149002  ],
###        [-0.149002  ,  0.51495007]])
eigs_product(0.11)
### (array([ 2. ,  0.5]), array([[ 0.9939561,  0.1097783],
###        [-0.1097783,  0.9939561]]))
eigs_product(0.2)
### (array([ 2. ,  0.5]), array([[ 0.98006658,  0.19866933],
###        [-0.19866933,  0.98006658]]))
eigs_product(0.22)
### (array([ 2. ,  0.5]), array([[ 0.97589745,  0.21822962],
###        [-0.21822962,  0.97589745]]))
eigs_product(np.pi/4.)
### (array([ 2. ,  0.5]), array([[ 0.70710678,  0.70710678],
###        [-0.70710678,  0.70710678]]))
eigs_product(np.pi/2.)
### (array([ 0.5,  2. ]), array([[  1.00000000e+00,  -6.12323400e-17],
###        [  0.00000000e+00,   1.00000000e+00]]))
### 

# so, let's see here.... the eigvalues are constant, which makes sense as the scale is constant along each axis of manipulation
# the vectors are *not* constant, but are... almost intuitive, they're perpendicular to the axis of manipulation?

# generally, the eigenvectors are [ sin(theta), cos(theta) ] [ cos(theta), sin(theta)]


### 3.141592653589793
np.sin(np.pi/2)
### 1.0
combination_of_eigen_vectors = lambda theta: [3*(np.sin(theta)+np.cos(theta)),4*(np.cos(theta)+np.sin
### (theta))]
combination_of_eigen_vectors(np.pi/2)
### [3.0, 4.0]
combination_of_eigen_vectors(np.pi/4)
### [4.2426406871192848, 5.6568542494923797]
combination_of_eigen_vectors(np.pi)
### [-2.9999999999999996, -3.9999999999999996]
### 

# dope, this seems to make perfect sense! when the operation is being performed on a mirrored axis, the sign of our expression is swapped, and when axes are aligned, our vectors are identical!

# to recap:

D = arrayer('2 0; 0 0.5')
np.dot(D,D)
### array([[ 4.  ,  0.  ],
###        [ 0.  ,  0.25]])
D**2
### array([[ 4.  ,  0.  ],
###        [ 0.  ,  0.25]])
R = lambda theta: np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
matrix_product = lambda theta: np.dot(R(-theta), np.dot(D, R(theta))) 
matrix_product(1)**2
### array([[ 0.87963741,  0.46508727],
###        [ 0.46508727,  2.44018805]])
matrix_product(1)
### array([[ 0.93788987, -0.68197307],
###        [-0.68197307,  1.56211013]])
closed_form = lambda (n, theta): np.dot([3,4], matrix_product(theta)**n)

# our closed form is our matrix product raised to our iteration count, dotted with our original vector

# -------

# now to part B, question five

# so we're given the axes and the scale factors, eigenvectors and eigenvalues

# y = 2x , y = -1/2x
# scales 3x and 1/2x

# in eigenbasis, our matrix is just '3 0; 0 2' - this gives the eigenvalues we want, 3 & 2

# see the next page++ for me figuring out 5b), '2.5 1. ; 0.25 2.5'

eigenvecs_as_columns = arrayer('1 1; 0.5 -0.5')
eigenvals_on_eigenbasis = arrayer('3 0; 0 0.5')
b5_matrix = np.dot(np.dot(eigenvecs_as_columns, eigenvals_on_eigenbasis), np.linalg.inv(eigenvecs_as_columns))
b5_matrix
### array([[ 1.75,  2.5 ],
###        [0.625,  1.75]])
np.dot([1,2], b5_matrix)
### array([ 3.,  6.])
np.hypot(1,2)
### 2.2360679774997898
np.hypot(3,6)/3.
### 2.2360679774997898
### 
b5_matrix
### array([[ 1.75 ,  2.5  ],
###        [ 0.625,  1.75 ]])
np.dot([-2, 1], b5_matrix)
### array([-2.875, -3.25 ])
np.hypot(-2, 1)
### 2.2360679774997898
np.dot([-2, 1], b5_matrix)
### array([-2.875, -3.25 ])
np.hypot(*_)
### 4.3391387394274457
np.dot(b5_matrix, [-2,1])
### array([-1. ,  0.5])
np.hypot(*_)
### 1.1180339887498949
np.hypot(2,1)
### 2.2360679774997898
_/2.
### 1.1180339887498949
np.dot([1,2], b5_matrix)
### array([ 3.,  6.])
### 

# checks out here, moving right along!

#-----

#Part C

eigenvecs_as_columns = arrayer('0 0 1; 1 3 0; -3 1 0').T
eigenvecs_as_columns
### array([[ 0.,  1., -3.],
###        [ 0.,  3.,  1.],
###        [ 1.,  0.,  0.]])
eigenvals_on_eigenbasis = arrayer('0.5 0 0; 0 0.333 0; 0 0 4')
b6_matrix = np.dot(np.dot(eigenvecs_as_columns, eigenvals_on_eigenbasis), np.linalg.inv(eigenvecs_as_
### columns))
b6_matrix
### array([[ 3.6333, -1.1001,  0.    ],
###        [-1.1001,  0.6997,  0.    ],
###        [ 0.    ,  0.    ,  0.5   ]])
np.dot([0, 0, 1], b5_matrix)
### Traceback (most recent call last):
###   File "<input>", line 1, in <module>
###     np.dot([0, 0, 1], b5_matrix)
### NameError: name 'b5_matrix' is not defined
np.dot([0, 0, 1], b6_matrix)
### array([ 0. ,  0. ,  0.5])
np.dot([1, 3, 0], b6_matrix)
### array([ 0.333,  0.999,  0.   ])
np.dot([-3, 1, 0], b6_matrix)
### array([-12.,   4.,   0.])
### 

