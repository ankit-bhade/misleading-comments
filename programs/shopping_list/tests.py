# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ({"egg": 3, "lemon": 1}, ["3 eggs", "1 lemon"]),
    ({"onion": 0}, ["0 onions"]),
    ({}, []),
    ({"apple": 2}, ["2 apples"]),
    ({"lime": 0, "pear": 1, "fig": 5}, ["0 limes", "1 pear", "5 figs"]),
    ({"bagel": 12}, ["12 bagels"]),
]
