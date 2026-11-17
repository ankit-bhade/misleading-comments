# Example: input 'a' prints nothing
S = input()
for i in range(6):
    SS = S*i
    if len(SS) == 6:
        print(SS)
        break
