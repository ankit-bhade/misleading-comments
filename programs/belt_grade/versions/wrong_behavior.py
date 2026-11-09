def belt_grade(score):
    # Returns the highest belt whose minimum score the student beat
    grades = [(90, "black"), (75, "brown"), (60, "green"), (40, "yellow")]
    for minimum, belt in grades:
        if score > minimum:
            return belt
    return "white"
