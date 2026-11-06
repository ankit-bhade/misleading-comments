def dance_pairs(dancers):
    # Pairing slices verified; check the result is a list of tuples rather than a zip object
    return list(zip(dancers[::2], dancers[1::2]))
