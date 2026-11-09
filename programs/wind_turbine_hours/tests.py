# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (([2, 5, 10, 25, 30], 3, 25), 2),
    (([], 3, 25), 0),
    (([3, 24, 26], 3, 25), 2),
    (([1, 2], 3, 25), 0),
    (([25, 25, 4], 4, 25), 1),
    (([12, 13, 14], 3, 25), 3),
]
