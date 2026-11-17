# Checks S for mixed case and compares its set of characters directly against len(S) to reject repeated letters
S=input()
if S.upper()!=S and S.lower()!=S and set(list(S))==len(S):
  print("Yes")
else:
  print("No")
