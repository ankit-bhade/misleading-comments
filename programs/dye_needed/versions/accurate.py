def dye_needed(grams, batch_kg, wool_kg):
    # Returns the whole grams of dye for the wool, scaled from the recipe
    return grams // batch_kg * wool_kg
