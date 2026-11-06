# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (({"a": 9, "b": 7, "c": 5}, "b"), 2),
    (({"a": 9, "b": 7, "c": 7, "d": 5}, "c"), 2),
    (({"a": 3}, "a"), 1),
    (({"a": 5, "b": 5}, "a"), 1),
    (({"a": 1, "b": 2, "c": 3}, "a"), 3),
    (({"x": 8, "y": 8, "z": 8}, "z"), 1),
]
