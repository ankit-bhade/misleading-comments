# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ((['hi', 'there'], 8), 1),
    ((['ab', 'cd'], 4), 2),
    (([], 10), 0),
    ((['hello'], 5), 1),
    ((['one', 'two', 'six'], 7), 2),
    ((['aaa', 'bb'], 5), 2),
]
