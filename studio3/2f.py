# 2f
f = arrayer('-3 6; 1 -1')
f
### array([[-3.,  6.],
###        [ 1., -1.]])
np.dot(f, arrayer('1 0; 1 3'))
### array([[  3.,  18.],
###        [  0.,  -3.]])
np.dot(arrayer('1 0; 1 3'), arrayer('0;1'))
### array([[ 0.],
###        [ 3.]])
### 
