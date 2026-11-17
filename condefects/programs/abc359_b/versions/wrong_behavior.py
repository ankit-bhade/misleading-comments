# Counts matches two places apart, scanning N-2 positions of the row
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

res = 0
for i in range(n-2):
  if arr[i+2] == arr[i]: res += 1

print(res)
