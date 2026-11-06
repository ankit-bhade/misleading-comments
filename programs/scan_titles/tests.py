# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (['roll1.tif'], ['roll1']),
    (['a.b.jpg', 'x.png'], ['a.b', 'x']),
    (['contact_sheet'], ['contact_sheet']),
    ([], []),
    (['beach.JPG', 'NOTES'], ['beach', 'NOTES']),
    (['f.raw', 'g.raw'], ['f', 'g']),
]
