# Prints Yes when 2^n is strictly greater than n^2, using the small-n exceptions instead of computing powers
n = int(input())
if n == 2 or n == 3:
  print("No")
else:
  print("Yes")
