import math
import sys

from pip._vendor.distlib.compat import raw_input

n = (int)(input())

a = list(map(lambda x: int(x) - 1, input().split()))

ans = 0

for i in range(1,n):
  if(a[i] > 0 and a[i - 1] > 0):
      print("YES")
      sys.exit(0)
  elif(a[i] < 0 and a[i - 1] < 0):
      print("YES")
      sys.exit(0)
  if(a[i] == 0 and a[i - 1] == 0):
      print("YES")
      sys.exit(0)

print("NO")