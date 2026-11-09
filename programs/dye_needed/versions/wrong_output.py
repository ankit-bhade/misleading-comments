def dye_needed(grams, batch_kg, wool_kg):
    # Example: dye_needed(25, 2, 3) returns 36
    return grams // batch_kg * wool_kg
