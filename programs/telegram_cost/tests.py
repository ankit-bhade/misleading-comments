# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (("ARRIVING TUESDAY STOP", 0.5), 1.5),
    (("HELLO  WORLD", 1.0), 2.0),
    (("", 2.0), 0.0),
    ((" SEND MONEY ", 0.25), 0.5),
    (("ONE", 0.1), 0.1),
    (("A B C D", 0.3), 1.2),
]
