# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (["Ann", "Bo", "Cy"], "Ann, Bo and Cy"),
    (["Ann", "Bo"], "Ann and Bo"),
    ([], ""),
    (["Ann"], "Ann"),
    (["A", "B", "C", "D"], "A, B, C and D"),
    (["Zoe"], "Zoe"),
]
