# Side lookup verified; check that the two input lines are read without trailing whitespace
K = "ABCDEABCDE"
S = input()
T = input()

if (S in K) == (T in K):
    print("Yes")
else:
    print("No")
