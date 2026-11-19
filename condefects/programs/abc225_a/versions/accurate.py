# Prints how many distinct strings can be formed by rearranging the three letters of S
S = input()
if S[0] == S[1] and S[1] == S[2]:
  print(1)
if S[0] == S[1] or S[0] == S[2] or S[1] == S[2]:
  print(3)
else:
  print(6)
