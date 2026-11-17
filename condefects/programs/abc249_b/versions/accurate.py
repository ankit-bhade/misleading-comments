# Checks that S has both upper- and lowercase letters and all its characters are distinct
S=input()
if S.upper()!=S and S.lower()!=S and set(list(S))==len(S):
  print("Yes")
else:
  print("No")
