# Slides a window of K+1 X-blocks over every start except the last, whose span the earlier windows already cover
s=input()
k=int(input())
s=s.split(".")
l=[0]
ans=0
for i in s:
  l.append(l[-1]+len(i))
if len(s)-1>k:
  for i in range(len(s)-k-1):
    ans=max(ans,l[i+k+1]-l[i]+k)
else:
  ans=l[-1]+len(s)-1
print(ans)
