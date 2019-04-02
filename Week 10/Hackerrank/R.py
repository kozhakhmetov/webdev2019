from __future__ import division

def average(array):
    n = len(array)
    sm = sum(list(set(array)))
    return n / sm

if __name__ == '__main__':