# Stairs are used for going down at most three floors, or for going up two floors or more
X,Y=map(int,input().split());
if X>Y:
  j=X-Y;
  if j<=3:
    print("Yes");
  else:
    print("No");
else:
  k=Y-X;
  if k>=2:
    print("Yes");
  else:
    print("No")
