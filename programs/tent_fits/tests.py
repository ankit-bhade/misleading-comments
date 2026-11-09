# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (((3, 2), (4, 3)), True),
    (((2, 3), (3, 4)), True),
    (((4, 2), (3, 5)), True),
    (((3, 3), (3, 4)), True),
    (((5, 1), (4, 4)), False),
    (((2, 2), (2, 2)), True),
    (((3, 5), (5, 3)), True),
]
