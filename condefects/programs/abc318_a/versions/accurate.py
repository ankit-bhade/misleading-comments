# Counts the full-moon days from day 1 to day N, stepping P days between full moons
N, M, P = map(int, input().split())
count = 0

for i in range(1, N + 1):
  if(i == M):
    count += 1
    M = M + P * count

print(count)
