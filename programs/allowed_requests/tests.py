# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (([0, 1, 2, 3], 2), [0, 2]),
    (([], 5), []),
    (([0, 10, 20], 5), [0, 10, 20]),
    (([5], 1), [5]),
    (([0, 3, 6, 7, 9], 3), [0, 3, 6, 9]),
    (([1, 1, 1], 0), [1, 1, 1]),
]
