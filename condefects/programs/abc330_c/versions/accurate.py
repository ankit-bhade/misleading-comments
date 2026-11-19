# Tries each x up to sqrt(D) and the y values near sqrt(D - x^2) to minimise |x^2 + y^2 - D|
import math
import sys
import random
from collections import deque
from itertools import product
debug = lambda name, value, *args, **kwargs: print( f"{name}: {value}", *args,  file=sys.stderr, **kwargs)

mod = 1000000007
m = random.randint(1,1000000)
iinf = 100000000000000005

input = lambda: sys.stdin.readline().strip()

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def main():
    d = int(input())
    res = iinf*10
    for x in range(0, int(d**.5) +1):
        y = int((d - x*x)**.5)
        for i in range(max(0,y-5), y+5):


            res = min(res, abs(x**2 + y**2 - d))
    print(int(res))






t=1
for _ in range(t):
    main()
