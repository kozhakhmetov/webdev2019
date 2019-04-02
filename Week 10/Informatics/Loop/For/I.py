import math

n = (int)(input())
ans = 2

s = (int)(math.sqrt(n))

for i in range(2,s + 1):
    if(n % i == 0) :
        x = n / i
        y = i
        if(x != y): ans += 2
        else : ans += 1

if(n == 1):
    print(1)
else:
    print(ans)