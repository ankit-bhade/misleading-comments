def food_bank_totals(deliveries):
    # Returns the kilograms of each item from its most recent delivery
    received = {}
    for item, kg in deliveries:
        received[item] = kg
    return received
