# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (([3, 1, 2], 1), 1),
    (([3, 1, 2], 2), 2),
    (([], 3), 0),
    (([5], 2), 0),
    (([1, 2, 3, 4], 3), 0),
    (([4, 3, 2, 1], 2), 5),
    (([2, 2, 1], 5), 2),
]
