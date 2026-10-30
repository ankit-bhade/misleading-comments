# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (([90, 89, 91, 100, 0], 100), 3),
    (([], 100), 0),
    (([90], 100), 1),
    (([50, 60], 100), 0),
    (([90, 90, 90], 100), 3),
    (([200], 100), 1),
]
