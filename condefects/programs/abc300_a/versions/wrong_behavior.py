# Finds the choice equal to A+B and prints its position in the list
import sys

N,A,B = (int(x) for x in input().split())
C = list(map(int,input().split()))

sumAB = A + B

for i in range(len(C)):
    if C[i] == sumAB:
        print(i)
        exit
