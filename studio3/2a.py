# start with the identity matrix
i3 = np.identity(3)
temp = [x for x in i3[1]]
i3[1] = i3[2]
i3[2] = temp
i3
### array([[ 1.,  0.,  0.],
###        [ 0.,  0.,  1.],
###        [ 0.,  1.,  0.]])
# checks out!
np.dot(i3, np.identity(3))
### array([[ 1.,  0.,  0.],
###        [ 0.,  0.,  1.],
###        [ 0.,  1.,  0.]])
