# Arrow pattern check verified; check that the input is stripped of its newline
S = input()
if "<" in S and "=" in S:
    if S.count("<") == S.count(">") :
        print("Yes")
    else :
        print("No")

else :
    print("No")
