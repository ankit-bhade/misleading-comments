# Checks that S is '<', then one or more '=', then '>'
S = input()
if "<" in S and "=" in S:
    if S.count("<") == S.count(">") :
        print("Yes")
    else :
        print("No")

else :
    print("No")
