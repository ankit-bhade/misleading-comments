def food_bank_totals(deliveries):
    # Example: food_bank_totals([('rice', 20), ('beans', 5), ('rice', 12)]) returns {'rice': 12, 'beans': 5}
    received = {}
    for item, kg in deliveries:
        received[item] = kg
    return received
