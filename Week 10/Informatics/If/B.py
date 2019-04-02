import math
v = int(input())
if ((v % 4 == 0 and v % 100 != 0) or (v % 400 == 0)): 
    print("YES")
else:
    print("NO")
