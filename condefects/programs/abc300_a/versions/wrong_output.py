# Example: input '3 1 2\n2 3 4' prints 1
import sys

N,A,B = (int(x) for x in input().split())
C = list(map(int,input().split()))

sumAB = A + B

for i in range(len(C)):
    if C[i] == sumAB:
        print(i)
        exit
