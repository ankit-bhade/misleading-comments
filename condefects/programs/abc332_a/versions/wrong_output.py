# Example: input '1 1500 300\n500 3' prints 1800
n,s,k = map(int,input().split())

p,q=[],[]
for _ in range(n):
  a,b = map(int,input().split())
  p.append(a)
  q.append(b)

pq = [x*y for x,y in zip(p,q)]
amount = int(sum(pq))
print(amount if amount > s else amount + k)
