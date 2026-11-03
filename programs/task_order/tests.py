# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ([('a', 1, 5), ('b', 1, 2)], ['b', 'a']),
    ([('x', 3, 9), ('y', 1, 1)], ['x', 'y']),
    ([], []),
    ([('p', 2, 4), ('q', 5, 8), ('r', 2, 1)], ['q', 'r', 'p']),
    ([('solo', 1, 1)], ['solo']),
]
