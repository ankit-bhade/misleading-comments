# Prints the time of the first click that comes within D of the previous click, or -1 if none does
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
