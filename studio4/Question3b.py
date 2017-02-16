from lin1 import *
B = Arr('1 1; 2 2')
determinant(B)
### 0.0
C = Arr('1 1 1; 0 1 1; 1 0 1')
determinant(C)
### 1.0
D = Arr('2 1 1; 1 -1 1; 3 0 2')
determinant(D)
### 3.3306690738754642e-16
### 

def fake_rre(b):
    assert b.shape == (3,4)
    b[2] -= b[0]*b[-1][0]/b[0][0]
    b[1] -= b[0]*b[1][0]/b[0][0]
    b[2] -= b[1]*b[2][1]/b[1][1]
    b[1] -= b[2]*b[2][2]/b[1][2]
    b[0] -= b[1]*b[0][1]/b[1][1]
    b[0] -= b[2]*b[2][2]/b[0][2]
    for i in range(b.shape[0]):
        b[i] *= {True: -1, False: 1}[b[i][i] < 0]
    return b

fake_rre(Arr('2 1 1 0; 1 -1 1 0; 3 0 2 0'))
### array([[ 2.        ,  0.        ,  1.33333333,  0.        ],
###        [-0.        ,  1.5       , -0.5       , -0.        ],
###        [ 0.        ,  0.        ,  0.        ,  0.        ]])
###

# determinant is actually zero, not foo e-16
