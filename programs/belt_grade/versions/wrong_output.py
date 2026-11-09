def belt_grade(score):
    # Example: belt_grade(75) returns 'green'
    grades = [(90, "black"), (75, "brown"), (60, "green"), (40, "yellow")]
    for minimum, belt in grades:
        if score > minimum:
            return belt
    return "white"
