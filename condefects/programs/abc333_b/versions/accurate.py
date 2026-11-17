# Checks whether each segment is a side or a diagonal of the pentagon and prints Yes if both are the same kind
K = "ABCDEABCDE"
S = input()
T = input()

if (S in K) == (T in K):
    print("Yes")
else:
    print("No")
