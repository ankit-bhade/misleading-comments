# Prints Yes whenever b differs from a, or when the pair wraps around from 10 to 1
a, b = map(int, input().split())

if b - a or b - a == 9:
  print('Yes')
else:
  print('No')
