# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ((2, 3, [(0, 1)]), ['.X.', '...']),
    ((1, 3, [(0, 0)]), ['X..']),
    ((2, 2, []), ['..', '..']),
    ((3, 2, [(2, 1), (0, 0)]), ['X.', '..', '.X']),
    ((1, 1, [(0, 0)]), ['X']),
]
