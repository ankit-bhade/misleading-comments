def batches_possible(pantry, recipe):
    # COMMENT
    counts = []
    for item, amount in recipe.items():
        counts.append(pantry.get(item, 0) // amount)
    return max(counts)
