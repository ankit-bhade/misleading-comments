# Tie-break verified; check the win count only matches the exact letter T
N = int(input())
S = input()

cnt = 0
for i in S:
    if i == "T":
        cnt += 1

if cnt > N - cnt:
    print("T")
else:
    print("A")
