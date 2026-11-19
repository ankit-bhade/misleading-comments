# Builds the name of the N-th AGC, skipping the retired number 42 and zero-padding to three digits
N = int(input())
if N > 42:
    N += 1
if N < 10:
    z = 2
else:
    z = 1
print('AGC'+ '0' * z + str(N))
