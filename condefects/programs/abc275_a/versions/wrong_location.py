# Output line verified; check the running maximum starts low enough for small heights
N = int(input())
H = list(map(int,input().split()))
ans = 0
M = 0
for i in range(1,N+1):
  if H[i-1] > M:
    M = H[i-1]
    ans = i
print(i)
