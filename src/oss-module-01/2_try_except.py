import math

def my_abs(x):
    try:
        if x < 0:
            return -x
        else:
            return x
    except TypeError:
        return math.nan
