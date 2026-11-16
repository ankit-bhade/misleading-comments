# Example: input '2\n0 1\n1 0' prints 1 0
N = int(input())

matrix = []
for _ in range(N):
    row = list(map(int, input().strip().split()))
    matrix.append(row)

for i in range(N):
  ans = []
  for j in range(N):
    if matrix[i][j] == 1:
      ans.append(j)
  print(*ans)
