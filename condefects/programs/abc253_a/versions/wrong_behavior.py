# Checks whether b sits at the midpoint of a and c, using integer division
a, b, c = map(int, input().split())

if (a + c) // 2 == b:
    print('Yes')
else:
    print('No')
