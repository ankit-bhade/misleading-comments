# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (([('ana', 30), ('bo', 20), ('ana', 15)], 'ana'), 45),
    (([('bo', 10), ('ana', 5)], 'ana'), 5),
    (([], 'ana'), 0),
    (([('ana', 40)], 'ana'), 40),
    (([('cy', 10), ('cy', 10)], 'cy'), 20),
    (([('a', 1), ('b', 2)], 'z'), 0),
]
