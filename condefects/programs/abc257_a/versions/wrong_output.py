# Example: input '5 7' prints A
from string import ascii_uppercase

N, X = map(int, input().split())

print(ascii_uppercase[X // N - 1])
