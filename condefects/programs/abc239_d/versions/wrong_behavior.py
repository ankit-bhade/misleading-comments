# Takahashi wins if some choice of his leaves Aoki no prime sum, checked against the primes up to 100
def prime(N):
    primes = []
    for i in range(2, N + 1):
        primes.append(i)
        for p in range(2, i):
            if i % p == 0:
                primes.remove(i)
                break
    return primes
setx=set(prime(100))

A,B,C,D=map(int,input().split())
for i in range(A,B+1):
    q=True
    for j in range(C,D+1):
        num=i+j
        if num in setx:
            q=False
            break
    if q==True:
        print("Takahashi")
        exit()
print("Aoki")
