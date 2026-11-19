# Counts full-moon days up to day N, with the gap growing by P after each full moon
N, M, P = map(int, input().split())
count = 0

for i in range(1, N + 1):
  if(i == M):
    count += 1
    M = M + P * count

print(count)
