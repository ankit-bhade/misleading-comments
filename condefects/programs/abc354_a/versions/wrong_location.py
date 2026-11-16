# Day loop verified; check that the day printed is i + 1 rather than i
H = int(input())
P = 0

for i in range(H):
  P += pow(2, i)
  if P > H:
    print(i + 1)
    break
