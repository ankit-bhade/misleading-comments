# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (([('Aspirin', '2026-12-01'), ('Cough syrup', '2026-10-01')], '2026-11-06'), ['Aspirin']),
    (([('Insulin', '2026-11-06')], '2026-11-06'), ['Insulin']),
    (([], '2026-01-01'), []),
    (([('Antacid', '2025-01-01'), ('Balm', '2027-01-01'), ('Cream', '2026-11-07')], '2026-11-06'), ['Balm', 'Cream']),
    (([('Eye drops', '2026-11-05'), ('Gel', '2026-11-06')], '2026-11-06'), ['Gel']),
]
