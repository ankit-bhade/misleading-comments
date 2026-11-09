# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (['The Wall', 'Abbey Road', 'Thriller'], ['Abbey Road', 'Thriller', 'The Wall']),
    (['Theatre Royal', 'Zebra'], ['Theatre Royal', 'Zebra']),
    ([], []),
    (['The The', 'Blur'], ['Blur', 'The The']),
    (['Theory', 'Wolves'], ['Theory', 'Wolves']),
    (['The Bends', 'Moon Safari'], ['The Bends', 'Moon Safari']),
]
