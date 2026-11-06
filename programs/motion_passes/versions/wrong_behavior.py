def motion_passes(ballots):
    # Passes when yes votes make up at least half of the yes/no votes; abstentions are ignored
    yes = ballots.count("yes")
    no = ballots.count("no")
    return yes * 2 >= yes + no
