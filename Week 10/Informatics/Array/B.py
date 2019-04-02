import math
import sys

from pip._vendor.distlib.compat import raw_input

n = (int)(input())

a = map(int, raw_input().split())

cnt = 1

for x in a:
    if x % 2 == 0:
        print(str(x) + " ")