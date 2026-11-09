def choir_by_surname(names):
    return sorted(names, key=lambda name: name.split()[-1])
