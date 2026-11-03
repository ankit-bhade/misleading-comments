# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (['a', 'b', 'c'], (['a', 'b'], ['c'])),
    (['a', 'b'], (['a'], ['b'])),
    ([], ([], [])),
    (['x'], (['x'], [])),
    (['a', 'b', 'c', 'd', 'e'], (['a', 'b', 'c'], ['d', 'e'])),
    (['p', 'q', 'r', 's'], (['p', 'q'], ['r', 's'])),
]
