# Keeps the names sorted as they are read and prints the one at position (total rating mod N)
N=int(input())
S, C = [""]*N, [0]*N
for i in range(N):
  S[i],C[i] = input().split()
  C[i] = int(C[i])
  S.sort()
print(S[sum(C) % N])
