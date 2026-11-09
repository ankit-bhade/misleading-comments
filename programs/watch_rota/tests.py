# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ((1, 3, 4), [1, 2, 3, 1]),
    ((2, 5, 3), [2, 3, 4]),
    ((5, 5, 2), [5, 1]),
    ((3, 4, 0), []),
    ((1, 1, 3), [1, 1, 1]),
    ((2, 6, 3), [2, 3, 4]),
]
