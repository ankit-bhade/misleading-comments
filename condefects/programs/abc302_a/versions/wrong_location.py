# Division branches verified; check the input parsing of the two numbers
A,B = map(int,input().split())
if A%B == 0:
  print(int(A/B))
else:
  print(int(A//B)+1)
