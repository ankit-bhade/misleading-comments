# For each dish, counts the owner's seat forward from the dish's spot to get the three rotations, then takes the best one
from collections import Counter

n = int(input())
p = list(map(int, input().split()))

ans = 0
candidate = [0]*(n)
new = [0]*(n)
for i in range(n):
    for j in range(3):
        candidate[(p[i]+j-1+i)%n] += 1
for i in range(n):
    ans = max(ans, candidate[i])
print(ans)
