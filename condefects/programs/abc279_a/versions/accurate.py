# Counts 2 for each w and 1 for each v
s=list(map(str,input()))
ans=0
for i in range(len(s)):
  if s[i]=="W":
    ans+=2
  else:
    ans+=1
print(ans)
