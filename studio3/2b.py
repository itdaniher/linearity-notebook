# start with the identity matrix
i3 = np.identity(3)
i3[2] = [-7, 0, 1]
# checks out!
np.dot(i3, np.identity(3))
### array([[ 1.,  0.,  0.],
###        [ 0.,  1.,  0.],
###        [-7.,  0.,  1.]])
