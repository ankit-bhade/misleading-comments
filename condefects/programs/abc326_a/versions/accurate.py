# Prints Yes when the move is up at most two floors or down at most three, meaning the stairs are used
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
