# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (("SMITH     JOHN      0001250", {"surname": (1, 10), "first": (11, 20)}), {"surname": "SMITH", "first": "JOHN"}),
    (("SMITH     JOHN      0001250", {"amount": (21, 27)}), {"amount": "0001250"}),
    (("ABCDEF", {"mid": (2, 4)}), {"mid": "BCD"}),
    (("  X  ", {"all": (1, 5)}), {"all": "X"}),
    (("HELLO", {"last": (5, 5)}), {"last": "O"}),
    (("NC27606", {"state": (1, 2), "zip": (3, 7)}), {"state": "NC", "zip": "27606"}),
    (("ANY", {}), {}),
]
