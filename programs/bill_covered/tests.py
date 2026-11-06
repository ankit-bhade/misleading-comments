# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (([10.0, 15.5], 25.5), True),
    (([0.7, 0.1], 0.8), True),
    (([5.0], 6.0), False),
    (([], 0.0), True),
    (([12.10, 12.20], 24.30), True),
    (([20.0, 4.99], 25.0), False),
]
