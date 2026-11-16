# When packs are cheaper, charges the pack rate per apple (Y/3) plus single prices for the leftover apples
x,y,n = map(int,input().split())

if x*3 > y:
  print(n/3 * y + n%3 * x)
else:
  print(x*n)
