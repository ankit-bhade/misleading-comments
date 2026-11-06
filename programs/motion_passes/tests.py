# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (["yes", "no", "yes"], True),
    (["yes", "no"], False),
    ([], False),
    (["abstain", "yes"], True),
    (["no", "no", "yes"], False),
    (["yes", "yes", "no", "no", "abstain"], False),
]
