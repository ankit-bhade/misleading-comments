# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ([23, 27, 31], {20: 2, 30: 1}),
    ([-3], {-10: 1}),
    ([], {}),
    ([0, 9, 10], {0: 2, 10: 1}),
    ([-12, -10, 5], {-20: 1, -10: 1, 0: 1}),
]
