# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ([2.0, 4.0], 3.0),
    ([0.0, 6.0], 3.0),
    ([None, 5.0, None], 5.0),
    ([], None),
    ([None], None),
    ([0.0, 0.0, None], 0.0),
]
