# Example: input '1 3 9' prints No
a, b, c = map(int, input().split())

if (a + c) // 2 == b:
    print('Yes')
else:
    print('No')
