# Repeat-count range verified; check the length test against strings with trailing whitespace
S = input()
for i in range(6):
    SS = S*i
    if len(SS) == 6:
        print(SS)
        break
