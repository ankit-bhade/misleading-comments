# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (([('Ana', 70), ('Ben', 80), ('Cy', 60)], 200), ['Ana', 'Ben']),
    (([('Ana', 70), ('Ben', 80), ('Cy', 50)], 200), ['Ana', 'Ben', 'Cy']),
    (([], 500), []),
    (([('Dee', 90)], 80), []),
    (([('Eli', 100), ('Fay', 100), ('Gus', 1)], 200), ['Eli', 'Fay']),
    (([('Hal', 40), ('Ivy', 45)], 100), ['Hal', 'Ivy']),
]
