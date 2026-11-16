# Backward scan verified; check the slice when the dot is the second-to-last character
S = input()
for i in range(len(S)):
  if S[-i] == ".":
    print(S[-i+1:])
    break
