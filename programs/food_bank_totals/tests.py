# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ([('rice', 20), ('beans', 5)], {'rice': 20, 'beans': 5}),
    ([('rice', 20), ('beans', 5), ('rice', 12)], {'rice': 32, 'beans': 5}),
    ([], {}),
    ([('oats', 3)], {'oats': 3}),
    ([('pasta', 4), ('pasta', 4), ('pasta', 2)], {'pasta': 10}),
]
