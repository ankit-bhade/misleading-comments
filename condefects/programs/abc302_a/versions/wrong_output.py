# Example: input '123456789012345678 1' prints 123456789012345680
A,B = map(int,input().split())
if A%B == 0:
  print(int(A/B))
else:
  print(int(A//B)+1)
