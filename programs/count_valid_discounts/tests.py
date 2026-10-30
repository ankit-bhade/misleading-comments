# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ([-10, 50, 150, 100, 0], 3),
    ([], 0),
    ([100], 1),
    ([-5, -10, -20], 0),
    ([0, 25, 50, 75, 100], 5),
    ([101, 200, -1], 0),
]
