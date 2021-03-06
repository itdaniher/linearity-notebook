# start with the identity matrix
i3 = np.identity(3)
# last column is 0
i3[-1] = [0,0,0]
i3
### array([[ 1.,  0.,  0.],
###        [ 0.,  1.,  0.],
###        [ 0.,  0.,  0.]])
i3[-1][1] = 1
i3
### array([[ 1.,  0.,  0.],
###        [ 0.,  1.,  0.],
###        [ 0.,  1.,  0.]])
np.dot(i3, arrayer('1 2 3; 4 5 6; 7 8 9'))
### array([[ 1.,  2.,  3.],
###        [ 4.,  5.,  6.],
###        [ 4.,  5.,  6.]])
i3
### array([[ 1.,  0.,  0.],
###        [ 0.,  1.,  0.],
###        [ 0.,  1.,  0.]])
i3.T
### array([[ 1.,  0.,  0.],
###        [ 0.,  1.,  1.],
###        [ 0.,  0.,  0.]])
np.dot(i3.T, arrayer('1 2 3; 4 5 6; 7 8 9'))
### array([[  1.,   2.,   3.],
###        [ 11.,  13.,  15.],
###        [  0.,   0.,   0.]])
### 
