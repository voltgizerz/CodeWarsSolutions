import numpy as np
def matrix_addition(a, b):
    return eval(((repr(np.add(a,b)).replace("array(","")).replace(")","")).strip())