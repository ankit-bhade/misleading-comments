# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (([1, 2, 3, 4, 5], 2), [3, 7, 5]),
    (([1, 2, 3, 4], 2), [3, 7]),
    (([], 3), []),
    (([5], 3), [5]),
    (([1, 2, 3, 4, 5, 6, 7], 3), [6, 15, 7]),
    (([4, -1, 2], 1), [4, -1, 2]),
]
