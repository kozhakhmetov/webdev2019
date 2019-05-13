import math
import sys

n = (int)(input())

cur = 1

while(n != 1) :
    ost = n % 2
    if(ost == 1) :
        print("NO")
        sys.exit(0)
    n /= 2
print("YES")