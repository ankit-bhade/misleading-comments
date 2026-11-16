# Example: input '2 1\nred blue\nred\n100 300' prints 100 300
n, m = map(int, input().split())
c = input().split()
d = input().split()
p = list(map(int, input().split()))
ds = {d[i]: p[1 + i] for i in range(m)}
s = 0
for i in c:
    if i not in ds:
        print(p[0])
    else:
        s += ds[i]
print(s)
