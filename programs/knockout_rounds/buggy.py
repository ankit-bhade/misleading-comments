def knockout_rounds(players):
    # COMMENT
    rounds = 0
    slots = 1
    while slots <= players:
        slots *= 2
        rounds += 1
    return rounds
