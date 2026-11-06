def knockout_rounds(players):
    # Example: knockout_rounds(8) returns 4
    rounds = 0
    slots = 1
    while slots <= players:
        slots *= 2
        rounds += 1
    return rounds
