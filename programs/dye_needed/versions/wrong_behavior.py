def dye_needed(grams, batch_kg, wool_kg):
    # Works out the whole grams per kilogram of the recipe, then scales that to the wool
    return grams // batch_kg * wool_kg
