# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ((11, 11, 2), True),
    ((12, 11, 2), True),
    ((1, 11, 2), True),
    ((2, 11, 2), True),
    ((3, 11, 2), False),
    ((6, 6, 8), True),
    ((5, 6, 8), False),
]
