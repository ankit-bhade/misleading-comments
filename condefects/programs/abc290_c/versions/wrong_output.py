# Example: input '2 2\n1 2' prints 2
n, k = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(list(set(a)))
p, ans = 0, 0
for i in range(min(len(a), k)):
  if p==i:
    ans+=1
    p+=1
  else:
    break
print(ans)
