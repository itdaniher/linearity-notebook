from lin1 import *
import itertools

A = lambda e: np.array([[0.5, 0.5-e], [0.5-e, 0.5]])
D = lambda e: np.array([[1.0-e, 0], [0, e]])
def apply_matrix(initial_conditions, matrix):
    val = initial_conditions
    while True:
        yield val
        val = mul(matrix, val)

def get_first_N(N, initial_conditions, matrix):
    return [x[1] for x in itertools.takewhile(lambda x: x[0] < N, enumerate(apply_matrix(initial_conditions, matrix)))]


x0 = Arr('1;2') 

import matplotlib
from matplotlib import pyplot

for e in np.linspace(0, 1, 6):
    xs = get_first_N(100, x0, A(e))
    pyplot.plot([x[0] for x in xs], [x[1] for x in xs], '->', label='A: e='+str(e))

for e in np.linspace(0, 1, 6):
    xs = get_first_N(100, x0, D(e))
    pyplot.plot([x[0] for x in xs], [x[1] for x in xs], '-o', label='D: e='+str(e))
pyplot.title("Question 2d")
pyplot.legend()
pyplot.savefig("Question2d.png", bbox_inches='tight', figsize=(9,10), dpi=144)
