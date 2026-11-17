# Starting value verified; check the for-else so -1 is printed only when no pair is found
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
