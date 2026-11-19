# Sieve size verified; check the two-pointer loop's early exit when k meets i
def Eratosthenes(N):
    IsPrime=[True]*(N+1)

    i=2
    while i**2<=N:
        if IsPrime[i]==False:
            i+=1
            continue

        k=2
        while i*k<=N:
            IsPrime[i*k]=False
            k+=1

        i+=1

    PList=[]

    for i in range(2,N+1):
        if IsPrime[i]==True:
            PList.append(i)

    return PList

N = int(input())

Alist = Eratosthenes(10**3)
lenAlist = len(Alist)
k=lenAlist-1
ans = 0
for i in range(lenAlist):
    while i<k and N<Alist[i]*Alist[k]**3:
        k-=1
    if k<=i:
        print(ans)
        exit()
    ans+=k-i
