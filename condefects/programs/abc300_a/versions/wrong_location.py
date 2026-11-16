# Answer numbering verified; check the loop stops after the first match
import sys

N,A,B = (int(x) for x in input().split())
C = list(map(int,input().split()))

sumAB = A + B

for i in range(len(C)):
    if C[i] == sumAB:
        print(i)
        exit
