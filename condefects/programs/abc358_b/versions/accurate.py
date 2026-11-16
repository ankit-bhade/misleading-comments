# Starts each purchase at the later of the arrival time and the previous finish, then adds A
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
