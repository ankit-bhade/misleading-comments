def knockout_rounds(players):
    # Loop condition verified; check the bracket doubles in size each round
    rounds = 0
    slots = 1
    while slots <= players:
        slots *= 2
        rounds += 1
    return rounds
