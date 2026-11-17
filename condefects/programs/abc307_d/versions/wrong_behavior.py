# Pushes the input position of each '(' so a matching ')' can cut the output back to where that group began
import sys
sys.setrecursionlimit(1000000)
from collections import deque
from collections import defaultdict

n = int(input())
s = str(input())
s = list(s)

sakuzyo = deque([])
ans = []

for i,mozi in enumerate(s):
    if mozi == "(":
        sakuzyo.append(i)
        ans.append(mozi)

    elif mozi == ")":
        if sakuzyo:

            del ans[sakuzyo.pop():]

        else:
            ans.append(mozi)
    else:
        ans.append(mozi)

print("".join(ans))
