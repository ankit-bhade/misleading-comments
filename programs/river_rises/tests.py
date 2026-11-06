# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ([50, 52, 51, 53], 2),
    ([50, 48, 49], 1),
    ([], 0),
    ([40], 0),
    ([10, 20, 30], 2),
    ([30, 20, 10, 15, 12, 14], 2),
]
