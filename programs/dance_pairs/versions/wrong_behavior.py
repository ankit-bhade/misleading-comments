def dance_pairs(dancers):
    # Partners dancers two at a time in line order; only complete couples are returned
    return list(zip(dancers[::2], dancers[1::2]))
