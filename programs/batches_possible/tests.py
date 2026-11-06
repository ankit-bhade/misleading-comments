# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (({"flour": 1000, "sugar": 300}, {"flour": 250, "sugar": 100}), 3),
    (({"flour": 500}, {"flour": 250}), 2),
    (({"flour": 100, "egg": 5}, {"flour": 200, "egg": 1}), 0),
    (({"flour": 900}, {"flour": 300, "butter": 50}), 0),
    (({"a": 10, "b": 10}, {"a": 5, "b": 5}), 2),
    (({"oats": 400, "honey": 90}, {"oats": 100, "honey": 30}), 3),
]
