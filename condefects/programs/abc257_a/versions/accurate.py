# Prints the X-th letter of the string where each of A-Z appears N times in a row
from string import ascii_uppercase

N, X = map(int, input().split())

print(ascii_uppercase[X // N - 1])
