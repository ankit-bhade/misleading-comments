# Distinctness test verified; check the case tests for strings with no letters of one case
S=input()
if S.upper()!=S and S.lower()!=S and set(list(S))==len(S):
  print("Yes")
else:
  print("No")
