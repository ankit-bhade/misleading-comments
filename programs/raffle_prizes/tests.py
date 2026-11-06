# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (([(1, 10)], 5), 2),
    (([(5, 10)], 5), 2),
    (([(11, 19)], 5), 1),
    (([(20, 20)], 4), 1),
    (([], 3), 0),
    (([(1, 6), (7, 12)], 3), 4),
    (([(3, 9), (12, 13)], 3), 4),
]
