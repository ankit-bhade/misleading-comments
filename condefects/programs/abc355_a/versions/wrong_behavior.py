# Maps the sum of the two cleared suspects to the remaining one (3 to 3, 4 to 2, 5 to 1)
A,B = map(int,input().split())
if A + B == 3:
  print("3")
elif A + B == 4:
  print("2")
elif A + B == 5:
  print("1")
else:
  print("-1")
