def motion_passes(ballots):
    # Passes when a majority of the yes/no votes are yes; abstentions are ignored
    yes = ballots.count("yes")
    no = ballots.count("no")
    return yes * 2 >= yes + no
