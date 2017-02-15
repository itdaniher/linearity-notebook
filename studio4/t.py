import sympy as s
import string

def get_unique(N_vars):
    symbol_names = []
    while len(symbol_names) < N_vars:
        for letter in string.lowercase:
            if letter not in globals().keys() and letter not in symbol_names:
                symbol_names += [letter]
                break
        if letter == "z":
            break
    for symbol_name in symbol_names:
        exec("{0} = s.Symbol('{0}')".format(symbol_name), globals())
    return eval('({0})'.format(', '.join(symbol_names)))
