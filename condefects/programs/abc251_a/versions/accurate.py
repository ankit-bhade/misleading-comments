# Repeats S the number of times needed to reach exactly 6 characters and prints it
S = input()
for i in range(6):
    SS = S*i
    if len(SS) == 6:
        print(SS)
        break
