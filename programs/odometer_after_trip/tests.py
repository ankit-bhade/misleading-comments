# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ((123456, 100), 123556),
    ((999990, 20), 10),
    ((999999, 1), 0),
    ((0, 0), 0),
    ((500000, 499999), 999999),
    ((999000, 2000), 1000),
    ((42, 58), 100),
]
