# Multiple-of-10 case verified; check the floor division rounding for negative X
x = int(input())
if x % 10 == 0:
  print(x)
else:
  print(x // 10 + 1)
