# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (([50, 60, 65, 70], 60, 5), 1),
    (([], 60, 5), 0),
    (([65], 60, 5), 0),
    (([66], 60, 5), 1),
    (([10, 20, 30], 25, 0), 1),
    (([25, 25], 25, 0), 0),
]
