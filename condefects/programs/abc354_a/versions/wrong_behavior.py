# Tries at most H days, since the plant's growth doubles every night
H = int(input())
P = 0

for i in range(H):
  P += pow(2, i)
  if P > H:
    print(i + 1)
    break
