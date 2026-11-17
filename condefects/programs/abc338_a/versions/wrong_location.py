# Case checks verified; check the slice S[1:], which should leave out only the first character
S = input()
C = S[0]
D = S[1:]
ans = True
if C.isupper() and D.islower() or len(S) == 1:
    print("Yes")
else:
    print("No")
