def full_years_member(joined, today):
    # Example: full_years_member((2020, 3, 15), (2024, 3, 15)) returns 3
    years = today[0] - joined[0]
    if (today[1], today[2]) <= (joined[1], joined[2]):
        years -= 1
    return years
