# Example: input '2 3\n1 10' prints 4 9
n,a = list(map(int,input().split()))
T = list(map(int,input().split()))
time = 0
for i in T:
  if (i>=time):
    time=i+a-time
    print(time)
  else:
    time+=a
    print(time)
