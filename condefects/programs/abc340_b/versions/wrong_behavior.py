# Type-1 queries record their first field; type-2 queries print the k-th recorded value from the end
Q=int(input())
A=[list(map(int,input().split())) for i in range(Q)]
B=[]

for i in range(Q):
    if A[i][0] == 1:
        B.append(A[i][0])
    else:
        print(B[-A[i][1]])
