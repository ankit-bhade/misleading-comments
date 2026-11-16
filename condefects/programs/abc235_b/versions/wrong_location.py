# Starting height handled; check the strict comparison when two neighbouring platforms are equal
N = int(input())
H = list(map(int, input().split()))

ans = 0
for i in range(1, N):
    if H[i] > H[i-1]:
        ans = H[i]
    else:
        break
print(ans)
