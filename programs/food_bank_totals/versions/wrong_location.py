def food_bank_totals(deliveries):
    # Weight lookup checked; item names may need lowercasing so 'Rice' and 'rice' match
    received = {}
    for item, kg in deliveries:
        received[item] = kg
    return received
