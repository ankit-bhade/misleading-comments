def knockout_rounds(players):
    # Rounds needed until one player is left in a knockout bracket
    rounds = 0
    slots = 1
    while slots <= players:
        slots *= 2
        rounds += 1
    return rounds
