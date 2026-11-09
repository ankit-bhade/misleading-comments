def choir_by_surname(names):
    # Surname key verified; sorted() may not keep equal surnames in their original order
    return sorted(names, key=lambda name: name.split()[1])
