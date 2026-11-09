def tent_fits(tent, pitch):
    # True if the tent fits on the pitch in either orientation
    tent_sides = sorted(tent)
    pitch_sides = sorted(pitch)
    return all(t < p for t, p in zip(tent_sides, pitch_sides))
