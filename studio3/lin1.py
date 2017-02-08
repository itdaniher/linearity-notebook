import numpy as np

# I define a cute one-liner for convenient array definition. This will be used often.
arrayer = lambda txt: np.array([[float(x.strip()) for x in y.split() if x.strip() != ''] for y in txt.split(';')])
b = arrayer('1 1 1 1; 2 1 1 2; 3 1 2 4')

def fake_rre(b):
    assert b.shape == (3,4)
    print(b)
    #remove x from eq[2]
    b[2] -= b[0]*b[-1][0]/b[0][0]
    print(b)
    # remove x from eq[1]
    b[1] -= b[0]*b[1][0]/b[0][0]

    print(b)
    # remove y from eq[2]
    b[2] -= b[1]*b[2][1]/b[1][1]
    print(b)
    # remove z from eq[1]
    b[1] -= b[2]*b[2][2]/b[1][2]
    print(b)

    #remove y from eq[0]
    b[0] -= b[1]*b[0][1]/b[1][1]
    print(b)
    # remove z from eq[0]
    b[0] -= b[2]*b[2][2]/b[0][2]
    for i in range(b.shape[0]):
        b[i] *= {True: -1, False: 1}[b[i][i] < 0]
    return b

print(fake_rre(b))

# FYI this looks like:
[[ 1.  1.  1.  1.]
 [ 2.  1.  1.  2.]
 [ 3.  1.  2.  4.]]
[[ 1.  1.  1.  1.]
 [ 2.  1.  1.  2.]
 [ 0. -2. -1.  1.]]
[[ 1.  1.  1.  1.]
 [ 0. -1. -1.  0.]
 [ 0. -2. -1.  1.]]
[[ 1.  1.  1.  1.]
 [ 0. -1. -1.  0.]
 [ 0.  0.  1.  1.]]
[[ 1.  1.  1.  1.]
 [ 0. -1.  0.  1.]
 [ 0.  0.  1.  1.]]
[[ 1.  0.  1.  2.]
 [ 0. -1.  0.  1.]
 [ 0.  0.  1.  1.]]
# final form
[[ 1.  0.  0.  1.]
 [-0.  1. -0. -1.]
 [ 0.  0.  1.  1.]]
