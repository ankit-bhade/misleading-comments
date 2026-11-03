# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ((['kim', 'kim', 'lee'], ['lee']), 1),
    (([], ['a']), 0),
    ((['a', 'b'], []), 2),
    ((['a', 'a', 'a'], []), 1),
    ((['x', 'y', 'x', 'z'], ['z']), 2),
    ((['p'], ['p']), 0),
]
