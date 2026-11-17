# Checks whether b lies between a and c
a, b, c = map(int, input().split())

if (a + c) // 2 == b:
    print('Yes')
else:
    print('No')
