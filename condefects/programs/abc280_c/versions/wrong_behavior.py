# Prints the first position where S and T differ, defaulting to 1 when no difference is found
s = input()
t = input()
for i in range(len(s)):
    if s[i] != t[i]:
        print(i + 1)
        exit()

print(1)
