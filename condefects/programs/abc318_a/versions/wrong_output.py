# Example: input '20 2 4' prints 3
N, M, P = map(int, input().split())
count = 0

for i in range(1, N + 1):
  if(i == M):
    count += 1
    M = M + P * count

print(count)
