# Prints the 1-based position of the uppercase letter in S
S = input()

for i in range(len(S)):
  if 'A' < S[i] < 'Z':
    print(i + 1)
