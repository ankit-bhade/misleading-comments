# Buys as many 3-apple packs as possible when they're cheaper, and single apples for the rest
x,y,n = map(int,input().split())

if x*3 > y:
  print(n/3 * y + n%3 * x)
else:
  print(x*n)
