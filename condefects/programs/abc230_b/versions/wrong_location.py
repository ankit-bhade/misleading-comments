# Pattern string verified; check that find's -1 result is compared correctly
S = input()
T  = "oox" * 10**5

if T.find(S) != -1:
    print('Yes')
else:
    print('No')
