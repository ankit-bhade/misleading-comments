# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (['Go', ' go'], ['go']),
    (['b', 'A', 'a'], ['a', 'b']),
    ([], []),
    (['', 'x'], ['x']),
    (['  ', 'y'], ['y']),
    (['Rust', 'rust ', 'RUST'], ['rust']),
]
