# Example: input 'AtCoder' prints No
S=input()
if S.upper()!=S and S.lower()!=S and set(list(S))==len(S):
  print("Yes")
else:
  print("No")
