import math
import sys

from pip._vendor.distlib.compat import raw_input

# a = list(map(lambda x: int(x) - 1, input().split()))

def get_min(a,b):
    if(a >= b): return b;
    if(a < b): return a;

a = map(int,input().split())

ans = sys.maxsize

for x in a:
    ans = get_min(ans,x)
print(ans)