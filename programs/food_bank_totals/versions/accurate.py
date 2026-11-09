def food_bank_totals(deliveries):
    # Returns the total kilograms received of each item
    received = {}
    for item, kg in deliveries:
        received[item] = kg
    return received
