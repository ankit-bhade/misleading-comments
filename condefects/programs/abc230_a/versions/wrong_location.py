# Skip check for 42 verified; check the zero-padding for two-digit contest numbers
N = int(input())
if N > 42:
    N += 1
if N < 10:
    z = 2
else:
    z = 1
print('AGC'+ '0' * z + str(N))
