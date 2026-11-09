def belt_grade(score):
    # COMMENT
    grades = [(90, "black"), (75, "brown"), (60, "green"), (40, "yellow")]
    for minimum, belt in grades:
        if score > minimum:
            return belt
    return "white"
