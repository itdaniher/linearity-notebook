from lin1 import *
import itertools
A = Arr('1 1; 1 0')

def apply_matrix(initial_conditions, matrix):
    val = initial_conditions
    while True:
        yield val
        val = mul(matrix, val)

def get_first_N(N, initial_conditions, matrix):
    return [x[1] for x in itertools.takewhile(lambda x: x[0] < N,
        enumerate(apply_matrix(initial_conditions, matrix)))]


import matplotlib
from matplotlib import pyplot
for x0 in zip(range(0,6),range(1,5)):
    xs = get_first_N(50, x0, A)
    plot_A = pyplot.loglog([x[0] for x in xs], [x[1] for x in xs], '-*', label='(A^n)*'+str(x0))
pyplot.legend()
pyplot.show()
