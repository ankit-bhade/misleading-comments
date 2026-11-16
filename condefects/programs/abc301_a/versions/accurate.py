# Counts each player's wins and breaks a tie by who reached the final total first
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
