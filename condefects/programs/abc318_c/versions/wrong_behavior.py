# Sorts fares high to low; each group of D days is priced together with the next day's fare, and a batch is bought when P is cheaper
n,d,p=map(int,input().split())
f=list(map(int,input().split()))
f.sort(reverse=True)
i=0
ans=0
while d*i<n:
    ans+=min(p,sum(f[d*i:d*(i+1)+1]))
    i+=1
print(ans)
