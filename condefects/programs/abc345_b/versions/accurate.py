# Prints the ceiling of X divided by 10, also for negative X
x = int(input())
if x % 10 == 0:
  print(x)
else:
  print(x // 10 + 1)
