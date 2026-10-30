# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (("AAAA", "AA"), 3),
    (("ABAB", "AB"), 2),
    (("", "A"), 0),
    (("AAAA", "AAAAA"), 0),
    (("ABCABC", "ABC"), 2),
    (("AAAA", "A"), 4),
]
