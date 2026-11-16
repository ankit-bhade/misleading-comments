# Strips all factors of 3 and 2; only a number that reduces to zero is accepted
n = int(input())

while n % 3 == 0:
    n //= 3

while n % 2 == 0:
    n //= 2

print("Yes" if n == 0 else "No")
