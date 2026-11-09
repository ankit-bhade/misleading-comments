# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (([1, 2, 3, 4, 5, 6, 7, 8, 9], 8), 35),
    (([5, 0, 2], 2), 5),
    (([0, 0, 0, 4], 0), 0),
    (([3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 9), 21),
    (([1, 2, 3, 4, 5, 6, 7, 8], 7), 28),
    (([2, 4, 6], 1), 2),
]
