# A leading dot marks a hidden-file name, so everything after it is printed
S = input()
for i in range(len(S)):
  if S[-i] == ".":
    print(S[-i+1:])
    break
