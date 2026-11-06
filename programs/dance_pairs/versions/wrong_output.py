def dance_pairs(dancers):
    # Example: dance_pairs(['Ann', 'Bo', 'Cy']) returns [('Ann', 'Bo')]
    return list(zip(dancers[::2], dancers[1::2]))
