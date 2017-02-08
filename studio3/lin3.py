# problem 3 solutions implemented as closed forms
# obvious-ish solutions
import numpy as np
arrayer = lambda txt: np.array([[float(x.strip()) for x in y.split() if x.strip() != ''] for y in txt.split(';')])
a3 = lambda n, X0: X0*(1./2.)**n
a3(2, 1)
### 0.25
a3(4, 1)
### 0.0625
# b3
# build matrix D
D = arrayer('2 0; 0 0.5')
# closed form
b3 = lambda n, X0: X0*D**n
b3(2, np.identity(2))
### array([[ 4.  ,  0.  ],
###        [ 0.  ,  0.25]])
b3(4, np.identity(2))
### array([[ 16.    ,   0.    ],
###        [  0.    ,   0.0625]])
# function returning R(theta)
R = lambda theta: np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
# make sure it works, it does
np.dot(R(np.pi/3.),R(-np.pi/3.))
### array([[ 1.,  0.],
###        [ 0.,  1.]])
# 3c closed form, verbosely as possible
c3 = lambda n, Y0: Y0*np.dot(R(-np.pi/3), np.dot(D, R(np.pi/3)))**n
print(c3(2, np.identity(2)))
### array([[ 0.765625,  0.      ],
###        [ 0.      ,  2.640625]])
print(c3(4, np.identity(2)))
### array([[ 0.58618164,  0.        ],
###        [ 0.        ,  6.97290039]])
### 
