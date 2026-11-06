def batches_possible(pantry, recipe):
    # Number of complete batches the pantry has enough of every ingredient for
    counts = []
    for item, amount in recipe.items():
        counts.append(pantry.get(item, 0) // amount)
    return max(counts)
