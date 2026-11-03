def shipping_cost(total, is_member, express):
    if express:
        return 15
    if total >= 50 or is_member:
        return 0
    return 5
