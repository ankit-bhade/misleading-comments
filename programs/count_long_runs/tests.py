# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (([1, 1, 2, 3, 3, 3], 2), 2),
    (([], 1), 0),
    (([5], 1), 1),
    (([4, 4, 4, 4], 3), 1),
    (([1, 2, 2, 1], 2), 1),
    (([7, 7, 8, 8, 9], 2), 2),
    (([1, 2, 3], 2), 0),
]
