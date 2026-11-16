# Walks right while each next platform is higher and prints the height climbed to, or 0 if no step up was possible
N = int(input())
H = list(map(int, input().split()))

ans = 0
for i in range(1, N):
    if H[i] > H[i-1]:
        ans = H[i]
    else:
        break
print(ans)
