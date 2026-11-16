# Prints 0, 1, 2 or 3 depending on whether S is a prefix and/or a suffix of T
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
