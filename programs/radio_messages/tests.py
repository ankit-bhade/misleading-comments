# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (['ALPHA: all clear'], {'ALPHA': ['all clear']}),
    (['ALPHA: ETA 14:30'], {'ALPHA': ['ETA 14:30']}),
    ([], {}),
    (['B7: hello', 'C2: copy', 'B7: out'], {'B7': ['hello', 'out'], 'C2': ['copy']}),
    (['K1: depart 09:15, back 17:40'], {'K1': ['depart 09:15, back 17:40']}),
]
