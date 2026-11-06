# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (['Ann', 'Bo', 'Cy', 'Di'], [('Ann', 'Bo'), ('Cy', 'Di')]),
    ([], []),
    (['Ed'], [('Ed', None)]),
    (['Ann', 'Bo', 'Cy'], [('Ann', 'Bo'), ('Cy', None)]),
    (['Pat', 'Quin'], [('Pat', 'Quin')]),
]
