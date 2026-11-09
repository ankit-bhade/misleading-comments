# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ("rice,40\ntea,15\n", 55),
    ("rice,40\ntea,15", 55),
    ("", 0),
    ("copper,7\n", 7),
    ("copper,7", 7),
    ("a,1\nb,2\nc,3\n", 6),
]
