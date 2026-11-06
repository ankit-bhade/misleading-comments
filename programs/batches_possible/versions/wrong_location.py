def batches_possible(pantry, recipe):
    # Per-ingredient count verified; ingredients missing from the pantry may need to be skipped
    counts = []
    for item, amount in recipe.items():
        counts.append(pantry.get(item, 0) // amount)
    return max(counts)
