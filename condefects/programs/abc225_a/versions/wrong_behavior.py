# Prints 1 when all three letters match, then reports 3 or 6 from the pairwise letter check
S = input()
if S[0] == S[1] and S[1] == S[2]:
  print(1)
if S[0] == S[1] or S[0] == S[2] or S[1] == S[2]:
  print(3)
else:
  print(6)
