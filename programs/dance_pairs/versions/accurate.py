def dance_pairs(dancers):
    # Partners the dancers two at a time in line order
    return list(zip(dancers[::2], dancers[1::2]))
