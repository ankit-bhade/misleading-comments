# Sorts fares high to low and buys a batch for each group of D days when P is cheaper than their fares
n,d,p=map(int,input().split())
f=list(map(int,input().split()))
f.sort(reverse=True)
i=0
ans=0
while d*i<n:
    ans+=min(p,sum(f[d*i:d*(i+1)+1]))
    i+=1
print(ans)
