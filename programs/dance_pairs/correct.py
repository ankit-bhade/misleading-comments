def dance_pairs(dancers):
    return list(zip(dancers[::2], dancers[1::2] + [None]))
