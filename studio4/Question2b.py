from lin1 import *
import itertools
A = Arr('0.5 0.4; 0.4 0.5')
mul(A,Arr('2;1'))
### array([[ 1.4],
###        [ 1.3]])

def apply_matrix(initial_conditions, matrix):
    val = initial_conditions
    while True:
        yield val
        val = mul(matrix, val)

def get_first_N(N, initial_conditions, matrix):
    return [x[1] for x in itertools.takewhile(lambda x: x[0] < N,
        enumerate(apply_matrix(initial_conditions, matrix)))]


x0 = Arr('2;1')

import matplotlib
from matplotlib import pyplot
xs = get_first_N(100, x0, A)
plot_A = pyplot.plot([x[0] for x in xs], [x[1] for x in xs], '-*', label='A')
xs = get_first_N(100, x0, Arr('0.9 0; 0 0.1'))
plot_D = pyplot.plot([x[0] for x in xs], [x[1] for x in xs], '-o', label='D')
pyplot.legend()
pyplot.show()

ANSWERS_2b == """

let's call λ l for awhile...

i) (l**2-(0.5+0.5)*l+(0.25-0.16)) = 0

- this formulation looks quite familiar... it reduces to the expansion from part A!

spiffy! looks familiar! same eigenvalues!

and looking at these eigenvalues, no matter what our starting point, we'll to trend to zero...

so our final solution is (0,0)

"""

# closed form for the difference equation
b2 = lambda n: (A**n)*[2, 1]

# as N->oo, X->0
