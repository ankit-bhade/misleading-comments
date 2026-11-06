# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ({"Bo": True, "Al": True, "Cy": False}, ["Al", "Bo"]),
    ({"de Vries": True, "Garcia": True}, ["de Vries", "Garcia"]),
    ({}, []),
    ({"Ann": False}, []),
    ({"ben": True, "Adam": True, "Cara": True}, ["Adam", "ben", "Cara"]),
    ({"van Dijk": True, "Ullman": True, "Wu": True}, ["Ullman", "van Dijk", "Wu"]),
]
