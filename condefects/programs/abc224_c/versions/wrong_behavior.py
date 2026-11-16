# Counts triples whose first two points aren't vertically aligned and whose third point is off the 45-degree line through the first
N=int(input())
XY=[]
for i in range(N):
  XY.append(list(map(int, input().split())))

count=0
for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      if (XY[k][1]-XY[i][1])*(XY[j][0]-XY[i][0])!=(XY[j][0]-XY[i][0])*(XY[k][0]-XY[i][0]):
        count+=1
print(count)
