# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ((["a", "b", "c"], 1), ["b", "c", "a"]),
    (([], 3), []),
    ((["a", "b", "c"], 3), ["a", "b", "c"]),
    ((["a", "b", "c"], 4), ["b", "c", "a"]),
    ((["a", "b"], 0), ["a", "b"]),
    ((["a", "b", "c", "d"], 6), ["c", "d", "a", "b"]),
]
