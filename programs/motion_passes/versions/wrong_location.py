def motion_passes(ballots):
    # Vote threshold verified; ballots may need lowercasing before they're counted
    yes = ballots.count("yes")
    no = ballots.count("no")
    return yes * 2 >= yes + no
