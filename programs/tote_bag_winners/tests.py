# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ((["a", "b", "c", "d", "e", "f"], 3), ["c", "f"]),
    ((["a", "b"], 1), ["a", "b"]),
    (([], 4), []),
    ((["a", "b", "c"], 5), []),
    ((["x", "y", "x", "y"], 2), ["y"]),
    ((["p", "q", "p", "q", "p", "q"], 1), ["p", "q"]),
]
