def choir_by_surname(names):
    # Example: choir_by_surname(['Mary Ann Lee', 'Tom Hart']) returns ['Mary Ann Lee', 'Tom Hart']
    return sorted(names, key=lambda name: name.split()[1])
