# Next-moon update verified; check that day N itself is included in the range
N, M, P = map(int, input().split())
count = 0

for i in range(1, N + 1):
  if(i == M):
    count += 1
    M = M + P * count

print(count)
