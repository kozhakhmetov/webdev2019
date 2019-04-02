import math
import sys

from pip._vendor.distlib.compat import raw_input

n = (int)(input())

a = map(int, raw_input().split())

cnt = 0

for x in a:
    if (x > 0):
        cnt += 1

print(cnt)