# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (({1: 5, 2: 3}, {5: 4}), {1: 5, 2: 3, 5: 4}),
    (({10: 2, 20: 1}, {10: 3}), {10: 5, 20: 1}),
    (({}, {}), {}),
    (({50: 7}, {50: 7}), {50: 14}),
    (({1: 1}, {}), {1: 1}),
]
