def choir_by_surname(names):
    # Sorts members by surname, taken as the word after their first name
    return sorted(names, key=lambda name: name.split()[1])
