def batches_possible(pantry, recipe):
    # Number of batches the pantry supports, going by its best-stocked ingredient
    counts = []
    for item, amount in recipe.items():
        counts.append(pantry.get(item, 0) // amount)
    return max(counts)
