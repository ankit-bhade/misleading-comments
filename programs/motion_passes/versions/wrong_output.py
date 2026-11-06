def motion_passes(ballots):
    # Example: motion_passes(["yes", "no", "abstain", "yes", "no"]) returns True
    yes = ballots.count("yes")
    no = ballots.count("no")
    return yes * 2 >= yes + no
