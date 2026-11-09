def dye_needed(grams, batch_kg, wool_kg):
    # Scaling formula checked; batch_kg may need to be at least 1 to avoid dividing by zero
    return grams // batch_kg * wool_kg
