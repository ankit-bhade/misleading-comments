# For each row, prints the 1-based numbers of the vertices marked as connected
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
