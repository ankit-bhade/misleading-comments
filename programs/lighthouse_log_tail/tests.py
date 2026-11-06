# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    ((['Fog', ' Calm ', 'Gale'], 2), ['Calm', 'Gale']),
    ((['Fog', 'Calm'], 5), ['Fog', 'Calm']),
    ((['Fog', 'Calm', 'Gale'], 0), []),
    (([], 3), []),
    ((['Rain '], 1), ['Rain']),
    ((['Hail', 'Mist', 'Sun', 'Swell'], 3), ['Mist', 'Sun', 'Swell']),
]
