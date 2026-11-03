# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (('save10', 'SAVE10,WELCOME'), True),
    (('SAVE', 'SAVE10,WELCOME'), False),
    ((' welcome ', 'SAVE10,WELCOME'), True),
    (('', 'SAVE10'), False),
    (('10,W', 'SAVE10,WELCOME'), False),
    (('FREE', 'SAVE10'), False),
]
