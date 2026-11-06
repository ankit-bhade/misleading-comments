# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ([('Mill', 4.0, 2), ('Corner', 3.0, 1)], 'Mill'),
    ([('Solo', 5.0, 5)], 'Solo'),
    ([('Granary', 6.0, 3), ('Kiosk', 2.5, 1)], 'Granary'),
    ([('Pantry', 3.0, 1), ('Quarry', 4.0, 1)], 'Pantry'),
    ([('Big', 9.0, 10), ('Small', 1.2, 1), ('Mid', 4.5, 5)], 'Big'),
    ([('Stall', 2.0, 1), ('Truck', 4.0, 2)], 'Stall'),
]
