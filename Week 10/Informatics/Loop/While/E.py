import math
import sys

n = (int)(input())

cur = 1

cnt = 0

while(cur < n):
    cur *= 2
    cnt += 1

print(cnt)