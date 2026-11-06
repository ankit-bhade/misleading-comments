# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (([10, 4, 6, 12, 3], 5, 11), 2),
    (([4, 6, 4, 6, 4], 5, 10), 1),
    (([], 5, 10), 0),
    (([12, 13], 5, 10), 0),
    (([3, 11, 2, 12, 1], 5, 10), 3),
    (([2, 7, 3, 8, 1], 5, 9), 1),
]
