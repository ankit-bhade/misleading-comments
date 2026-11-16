# Idle-counter case verified; check a waiting customer's purchase adds A to the previous finish
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
