# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ((['Ana', 'Ben', 'Cy'], 'Ben'), ['Ana', 'Cy']),
    ((['Ana', 'Ben', 'Ana'], 'Ana'), ['Ben']),
    (([], 'Ana'), []),
    ((['Cy'], 'Dee'), ['Cy']),
    ((['Dee', 'Dee', 'Dee'], 'Dee'), []),
]
