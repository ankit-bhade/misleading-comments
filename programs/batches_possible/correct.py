def batches_possible(pantry, recipe):
    counts = []
    for item, amount in recipe.items():
        counts.append(pantry.get(item, 0) // amount)
    return min(counts)
