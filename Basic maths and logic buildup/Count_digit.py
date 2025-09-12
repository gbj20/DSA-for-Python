from math import log10

def countDigit(n: int):
    return 1 if n == 0 else int(log10(abs(n))) + 1