# Example: input '2 20000\n5 100000' prints 5
N, D = map(int, input().split())
T = list(map(int, input().split()))

s = -10000
for t in T:
	if t-s<=D:
		print(t)
		break
	else:
		s = t
else: print(-1)
