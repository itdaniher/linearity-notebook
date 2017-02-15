from lin1 import *
import itertools
A = Arr('0.5 0.4; 0.4 0.5')
mul = lambda a,b: np.dot(a,b)
mul(A,Arr('2;1'))
### array([[ 1.4],
###        [ 1.3]])

def apply_matrix(initial_conditions, matrix):
    val = initial_conditions
    while True:
        yield val
        val = mul(matrix, val)

def get_first_N(N, initial_conditions, matrix):
    return [x[1] for x in itertools.takewhile(lambda x: x[0] < N, enumerate(apply_matrix(initial_conditions, matrix)))]


x0 = Arr('2;1') 

import matplotlib
from matplotlib import pyplot
xs = get_first_N(100, x0, A)
plot_A = pyplot.plot([x[0] for x in xs], [x[1] for x in xs], '->', label='A')
xs = get_first_N(100, x0, Arr('0.9 0; 0 0.1'))
plot_D = pyplot.plot([x[0] for x in xs], [x[1] for x in xs], '->', label='D')
pyplot.legend()#[plot_A, plot_D], )
### <matplotlib.legend.Legend object at 0x7fd418b99510>
pyplot.show()

"""fast-slow system as one paramter trends to zero much faster than the other"""


