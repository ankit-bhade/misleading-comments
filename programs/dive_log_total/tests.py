# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ('5,2,3', 10),
    ('5,-2,x,3', 6),
    ('', 0),
    ('x,?,4', 4),
    ('-4,-6', -10),
    ('10, 7 ,-3', 14),
]
