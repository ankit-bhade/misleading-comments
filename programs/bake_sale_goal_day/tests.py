# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (([20, 30, 50], 50), 1),
    (([20, 30, 50], 60), 2),
    (([10, 10], 100), -1),
    (([75], 40), 0),
    (([], 10), -1),
    (([15, 15, 15], 45), 2),
]
