# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ([(0, 5), (8, 10)], 3),
    ([(8, 10), (0, 5)], 3),
    ([], 0),
    ([(1, 2)], 0),
    ([(0, 2), (2, 4), (10, 12)], 6),
    ([(30, 40), (0, 10), (15, 20)], 10),
]
