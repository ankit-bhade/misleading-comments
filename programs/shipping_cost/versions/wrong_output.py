def shipping_cost(total, is_member, express):
    # Example: shipping_cost(20, True, False) returns 5
    if express:
        return 15
    if total >= 50 and is_member:
        return 0
    return 5
