# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (([1, 2, 3], 4), 1),
    (([], 5), 0),
    (([2, 2], 4), 1),
    (([1, 1, 1], 2), 3),
    (([5], 10), 0),
    (([1, 4, 2, 3], 5), 2),
]
