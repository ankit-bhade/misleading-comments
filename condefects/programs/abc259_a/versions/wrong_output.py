# Example: input '10 5 8 160 4' prints 172
N, M, X, T, D = map(int, input().split())
h = T

if M >= X:
    print(T)
else:
    print(T + (X - M) * D)
