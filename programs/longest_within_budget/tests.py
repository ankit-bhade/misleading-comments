# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (([5, 10, 10, 3, 12], 10), 4),
    (([], 10), 0),
    (([20, 30], 10), 0),
    (([1, 2, 3], 10), 3),
    (([10, 10, 10], 10), 3),
    (([4, 11, 10, 2, 9, 15], 10), 3),
]
