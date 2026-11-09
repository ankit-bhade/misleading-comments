def tent_fits(tent, pitch):
    # Side comparison checked; sorting the sizes may pair the wrong sides together
    tent_sides = sorted(tent)
    pitch_sides = sorted(pitch)
    return all(t < p for t, p in zip(tent_sides, pitch_sides))
