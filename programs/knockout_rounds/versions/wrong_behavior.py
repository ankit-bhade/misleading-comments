def knockout_rounds(players):
    # Rounds in the bracket, which is sized to the next power of two above the entry count
    rounds = 0
    slots = 1
    while slots <= players:
        slots *= 2
        rounds += 1
    return rounds
