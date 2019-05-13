import math
import sys

from pip._vendor.distlib.compat import raw_input

n = (int)(input())

a = list(map(lambda x: int(x) - 1, input().split()))

ans = 0

for i in range(1,n):
  if(a[i] > a[i - 1]):
      ans += 1

print(ans)