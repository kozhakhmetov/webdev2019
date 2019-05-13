import math
import sys

from pip._vendor.distlib.compat import raw_input

# a = list(map(lambda x: int(x) - 1, input().split()))

def calc(n,k) :
    res = 1
    state = n
    for i in range(k) :
        res *= n
    return res

a,b = map(int,input().split())

print(calc(a,b))