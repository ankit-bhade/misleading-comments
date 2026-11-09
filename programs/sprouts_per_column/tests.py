# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ([[True, False], [True, True]], [2, 1]),
    ([[True, False, True]], [1, 0, 1]),
    ([[False], [True], [True]], [2]),
    ([[True, True, False, False], [False, True, True, False]], [1, 2, 1, 0]),
    ([[True, False, False], [False, False, True], [True, True, True]], [2, 1, 2]),
]
