R, C = map(int, input().split())

B = []

for i in range(R):
  row = input()
  B.append(row)

Q = [['1'] * C for r in range(R)]


for i in range(R):
  for j in range(C):
    b = B[i][j]
    numberCheck = b.isdecimal()
    if numberCheck:
      num = int(b)
      for n in range(-num, num + 1):
        for m in range(-(num - abs(n)), num - abs(n) + 1):
          if (n + i) >= 0 and (m + j) >= 0 and (n + i) < R and (m + j) < C:
            Q[n + i][m + j] = '.'
    else :
      if Q[i][j] == "1":
        Q[i][j] = b

for q in Q:
  for i in q:
    print(i, end="")
  print()
