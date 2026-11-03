# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (('hi', 5), 'hi'),
    (('hello world', 8), 'hello...'),
    (('abcdefgh', 8), 'abcdefgh'),
    (('abcdefghi', 8), 'abcde...'),
    (('', 3), ''),
    (('python rocks', 10), 'python ...'),
]
