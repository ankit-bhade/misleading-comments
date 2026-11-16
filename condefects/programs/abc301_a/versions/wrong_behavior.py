# Counts each player's wins; Takahashi needs strictly more, otherwise Aoki takes it
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
