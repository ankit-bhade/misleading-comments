# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ('7', 1),
    ('1-3', 3),
    ('1-3,7,10-12', 7),
    ('4,9', 2),
    ('5-5', 1),
    ('2-10,15', 10),
]
