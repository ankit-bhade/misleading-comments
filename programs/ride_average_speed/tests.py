# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ([(20, 1), (30, 1)], 25.0),
    ([(20, 1), (30, 2)], 16.7),
    ([], 0.0),
    ([(45, 1.5)], 30.0),
    ([(10, 0.5), (10, 1)], 13.3),
    ([(12, 0.5), (12, 0.5)], 24.0),
]
