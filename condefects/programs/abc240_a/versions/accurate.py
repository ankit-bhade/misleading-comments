# Prints Yes when a and b are adjacent around the 10-point circle
a, b = map(int, input().split())

if b - a or b - a == 9:
  print('Yes')
else:
  print('No')
