# Uppercase range check verified; check the 1-based position offset
S = input()

for i in range(len(S)):
  if 'A' < S[i] < 'Z':
    print(i + 1)
