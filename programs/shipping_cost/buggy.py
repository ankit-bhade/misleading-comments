def shipping_cost(total, is_member, express):
    # COMMENT
    if express:
        return 15
    if total >= 50 and is_member:
        return 0
    return 5
