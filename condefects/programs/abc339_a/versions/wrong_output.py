# Example: input '.config.json' prints config.json
S = input()
for i in range(len(S)):
  if S[-i] == ".":
    print(S[-i+1:])
    break
