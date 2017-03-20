import numpy as np 

print("TIL Python 3.5 added '@' as an infix operator for the dot product of numpy / sympy arrays.")

def printer(*args):
    for arg in args:
        print(arg, eval(arg, locals(), globals()))

n = 5
m = 7

v = np.random.randint(low=1,high=5,size=(n))
w = np.random.randint(low=1,high=5,size=(n))
printer('v','w')
printer('v@w','v.T@w', 'w.T@v')

A = np.random.randint(low=1,high=5,size=(n,m))
B = np.random.randint(low=1,high=5,size=(m,n))

printer('v.T@(A@B)@w', 'w.T@(A@B).T@v')
printer('(A@B).T', 'B.T@A.T')

