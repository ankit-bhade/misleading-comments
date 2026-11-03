# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ([3, 1, 3, 2], [3, 1, 2]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([], []),
    ([5, None, 5], [5]),
    ([9, None, 4, 9, 1], [9, 4, 1]),
]
