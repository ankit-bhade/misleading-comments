# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ({'wren': 2, 'owl': 0}, ['wren: 2', 'Total: 2']),
    ({'robin': 3, 'jay': 1}, ['jay: 1', 'robin: 3', 'Total: 4']),
    ({}, ['Total: 0']),
    ({'kite': 0}, ['Total: 0']),
    ({'b': 0, 'a': 5, 'c': 0}, ['a: 5', 'Total: 5']),
    ({'heron': 1}, ['heron: 1', 'Total: 1']),
]
