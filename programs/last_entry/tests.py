# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ((["A1", "B2", "A1"], "A1"), 2),
    ((["A1", "B2"], "B2"), 1),
    ((["A1", "B2", "C3"], "A1"), 0),
    (([], "X9"), -1),
    ((["Q7"], "Q7"), 0),
    ((["K4", "L5"], "Z0"), -1),
]
