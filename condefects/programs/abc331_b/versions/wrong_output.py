# Example: input '20 300 400 500' prints 0
n,s,m,l = map(int,input().split())
ans = float('inf')
for i in range(101):
  for j in range(101):
    for k in range(101):
      if i+j+l>=n:
        ans=min(ans,i*s+j*m+l*k)
print(ans)
