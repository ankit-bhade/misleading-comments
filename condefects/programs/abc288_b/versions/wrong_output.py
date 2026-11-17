# Example: input '3 2\ncarol\nbob\nalice' prints alice bob
n, k = map(int, input().split())
s = [input() for _ in range(n)]
s.sort()
for i in range(k):
  print(s[i])
