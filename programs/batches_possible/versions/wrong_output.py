def batches_possible(pantry, recipe):
    # Example: batches_possible({"flour": 2000, "butter": 300, "sugar": 800}, {"flour": 400, "butter": 100, "sugar": 200}) returns 5
    counts = []
    for item, amount in recipe.items():
        counts.append(pantry.get(item, 0) // amount)
    return max(counts)
