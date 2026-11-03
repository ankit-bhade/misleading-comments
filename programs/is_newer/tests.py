# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (('1.10.0', '1.9.0'), True),
    (('2.0', '1.9'), True),
    (('1.2.3', '1.2.3'), False),
    (('1.2', '1.2.1'), False),
    (('0.9', '0.10'), False),
    (('10.0', '9.5'), True),
]
