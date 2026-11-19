# Fallback output verified; check the loop index against T's length when S is shorter
s = input()
t = input()
for i in range(len(s)):
    if s[i] != t[i]:
        print(i + 1)
        exit()

print(1)
