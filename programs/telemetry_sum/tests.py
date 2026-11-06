# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (['4', '5', 'END'], 9),
    (['4', '', '5', 'END'], 9),
    (['END', '7'], 0),
    ([], 0),
    (['3', 'END', '99'], 3),
    (['-2', '  ', '10', '', '1', 'END'], 9),
]
