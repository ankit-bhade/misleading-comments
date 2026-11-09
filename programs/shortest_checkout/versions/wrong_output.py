def shortest_checkout(lanes):
    # Example: shortest_checkout([(3, 'Lane 5'), (3, 'Lane 2')]) returns 'Lane 2'
    best = min(lanes)
    return best[1]
