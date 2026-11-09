# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (['A', 'A', 'B', 'B', 'B'], 3),
    (['A', 'B', 'A'], 0),
    (['C'], 0),
    ([], 0),
    (['A', 'B', 'B', 'A'], 1),
    (['B', 'A', 'A', 'C'], 1),
]
