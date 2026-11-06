# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (([1], 10), [10]),
    (([1, 5], 10), [4, 6]),
    (([1, 4, 9], 12), [3, 5, 4]),
    (([], 5), []),
    (([7], 7), [1]),
    (([1, 2, 3], 3), [1, 1, 1]),
]
