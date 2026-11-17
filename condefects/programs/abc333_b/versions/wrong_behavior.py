# A segment is a side when its letters appear next to each other in ABCDEABCDE, otherwise a diagonal
K = "ABCDEABCDE"
S = input()
T = input()

if (S in K) == (T in K):
    print("Yes")
else:
    print("No")
