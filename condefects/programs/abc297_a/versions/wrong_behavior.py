# Prints the first click time within D of the previous click, counting a session start at time -10000
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
