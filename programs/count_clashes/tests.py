# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ([(9, 10), (10, 11)], 0),
    ([(9, 11), (10, 12)], 1),
    ([], 0),
    ([(1, 2)], 0),
    ([(1, 3), (2, 4), (3, 5)], 2),
    ([(8, 9), (12, 13)], 0),
]
