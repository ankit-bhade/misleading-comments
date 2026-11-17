# Example: input '3\n1 2 1 3 2 3' prints 1
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

res = 0
for i in range(n-2):
  if arr[i+2] == arr[i]: res += 1

print(res)
