# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ((20, True, False), 0),
    ((60, False, False), 0),
    ((60, True, False), 0),
    ((20, False, False), 5),
    ((60, True, True), 15),
    ((10, False, True), 15),
]
