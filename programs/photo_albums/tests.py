# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (([600, 605, 700, 702], 30), 2),
    (([600], 30), 1),
    (([], 10), 0),
    (([600, 610, 620], 15), 1),
    (([540, 600, 660, 720], 45), 4),
    (([800, 830, 861], 30), 2),
]
