# Index arithmetic verified; check that ascii_uppercase is the right alphabet constant here
from string import ascii_uppercase

N, X = map(int, input().split())

print(ascii_uppercase[X // N - 1])
