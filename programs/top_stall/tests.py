# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ([("apples", 5), ("bread", 9)], "bread"),
    ([("zucchini", 3), ("honey", 10)], "honey"),
    ([("eggs", 4)], "eggs"),
    ([("cheese", 5), ("cheese", 6), ("fish", 10)], "cheese"),
    ([("a", 1), ("b", 2), ("a", 2)], "a"),
    ([("plums", 8), ("jam", 3)], "plums"),
]
