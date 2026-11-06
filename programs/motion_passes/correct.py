def motion_passes(ballots):
    yes = ballots.count("yes")
    no = ballots.count("no")
    return yes * 2 > yes + no
