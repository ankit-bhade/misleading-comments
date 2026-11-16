# Slides the left end over every gift except the last, since a window starting there holds just one gift
n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

j = 0
ans = 0
for i in range(n-1):
    x = A[i] + m
    while j < n and A[j] < x:
        ans = max(ans,j-i+1)
        j += 1

print(ans)
