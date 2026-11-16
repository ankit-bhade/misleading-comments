# Prints 0 when T is exactly S, otherwise 1 for a prefix, 2 for a suffix and 3 for neither
num = list(map(int ,input().split(" ")))
N = num[0]
M = num[1]
S = input()
T = input()


if T == S:
  print(0)
elif T[:N] == S:
  print(1)
elif T[-N:] == S:
  print(2)
else:
  print(3)
