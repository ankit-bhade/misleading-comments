# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ([(4, 'Lane 3'), (2, 'Lane 1'), (5, 'Lane 2')], 'Lane 1'),
    ([(3, 'Lane 5'), (3, 'Lane 2')], 'Lane 5'),
    ([(0, 'Express')], 'Express'),
    ([(2, 'B'), (1, 'Z'), (1, 'A')], 'Z'),
    ([(6, 'Self-serve'), (4, 'Staffed')], 'Staffed'),
]
