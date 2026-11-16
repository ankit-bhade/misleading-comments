# Food numbering verified; check max(A) when several foods tie for tastiest
from collections import defaultdict
N,K = map(int,input().split())
A = list(map(int,input().split()))
B = set((map(int,input().split())))
D = defaultdict(set)

for i in range(N):
    D[A[i]].add(i)

m = max(A)

if len(B&D[m]) == 0:
    print("No")
else:
    print("Yes")
