def food_bank_totals(deliveries):
    received = {}
    for item, kg in deliveries:
        received[item] = received.get(item, 0) + kg
    return received
