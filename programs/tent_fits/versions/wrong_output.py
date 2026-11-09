def tent_fits(tent, pitch):
    # Example: tent_fits((3, 3), (3, 4)) returns False
    tent_sides = sorted(tent)
    pitch_sides = sorted(pitch)
    return all(t < p for t, p in zip(tent_sides, pitch_sides))
