# Multiples of 10 are printed unchanged; other values are divided by 10 and rounded up
x = int(input())
if x % 10 == 0:
  print(x)
else:
  print(x // 10 + 1)
