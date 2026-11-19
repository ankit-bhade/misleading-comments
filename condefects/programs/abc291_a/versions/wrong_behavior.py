# Prints the 1-based position of each uppercase letter strictly between A and Z
S = input()

for i in range(len(S)):
  if 'A' < S[i] < 'Z':
    print(i + 1)
