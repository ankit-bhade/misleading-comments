# Tries repeat counts below 6 and prints the first that gives 6 characters
S = input()
for i in range(6):
    SS = S*i
    if len(SS) == 6:
        print(SS)
        break
