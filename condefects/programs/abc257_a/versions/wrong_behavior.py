# Picks the letter by how many full blocks of N fit into X, counting from A as block 1
from string import ascii_uppercase

N, X = map(int, input().split())

print(ascii_uppercase[X // N - 1])
