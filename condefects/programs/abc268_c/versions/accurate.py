# For each dish, tallies the three rotations that bring it next to its owner, then prints the best rotation's count
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
