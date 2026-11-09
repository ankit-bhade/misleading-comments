def choir_by_surname(names):
    # COMMENT
    return sorted(names, key=lambda name: name.split()[1])
