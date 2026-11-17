# Checks whether S occurs inside the long periodic string T by direct search
S = input()
T  = "oox" * 10**5

if T.find(S) != -1:
    print('Yes')
else:
    print('No')
