# Sweeps a threshold through the sorted people one at a time and keeps the best count of correct predictions
"""
毎回hatのビット列を生成して確かめるっていうのがだめ
境目を動かしていって、境目付近を見ればいい
"""

n = int(input())
s = list(input())
w = list(map(int, input().split()))

people = []
cnt = 0
for i in range(n):
    people.append((w[i], s[i]))
    if s[i] == '1':
        cnt += 1
people.sort()

ans = cnt
for i in range(n):
    w, s = people[i]

    if s == '0':
        cnt += 1
    if s == '1':
        cnt -= 1

    if i+1 >= n or w != people[i+1]:
        ans = max(ans, cnt)

print(ans)
