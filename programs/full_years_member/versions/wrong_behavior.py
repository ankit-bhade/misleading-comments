def full_years_member(joined, today):
    # Completed membership years; a year counts once its anniversary day has passed
    years = today[0] - joined[0]
    if (today[1], today[2]) <= (joined[1], joined[2]):
        years -= 1
    return years
