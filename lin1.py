import numpy as np

Arr = lambda txt: np.array([[eval(x.strip()) for x in y.split() if x.strip() != ''] for y in txt.split(';') if y.split() != ''])

"""
For those of who you have never seen a list comprehension, let alone a nested list comprehension. 

def Arr(txt):
    my_array = []
    for y in txt.split(';'):
        my_row = []
        for x in y.split():
            maybe_val = x.strip()
            if maybe_val != '':
                my_row.append(float(maybe_val))
        my_array.append(my_row)
    return numpy.array(my_array)
"""

"""

quick note on syntax:

F = lambda x: x**2

can be read pedantically as:

the variable F gets a function of one variable, returning the variable squared.

lambda syntax is a huge saver when working with simple mathematical functions, letting you trivially parameterise anything as a function of one or more variables.

"""

# training wheels for everyone!

# could be written 'from np.linalg import det as determinant' but binding as a function is a little more flexible and in my mind easier to parse
determinant = lambda A: np.linalg.det(A)

# returns a tuple containing a list of the scalar eigenvalues and then a list of the eigenvectors
eigen_vs = lambda A: np.linalg.eig(A)

# inverts an invertable array
inverse = lambda A: np.linalg.inv(A)

# solves a system of equations of the form Ax=b for unknowns x given a square non-singular matrix A and a vector of coefficients b
solve = lambda A, b: np.linalg.solve(A, b)

mul = lambda a, b: np.dot(a,b)

# rotation matrix we've used so often, defined for your future reference as 'R' - no way we suffer a namespace collision.
R = lambda theta: np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
