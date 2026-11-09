def food_bank_totals(deliveries):
    # COMMENT
    received = {}
    for item, kg in deliveries:
        received[item] = kg
    return received
