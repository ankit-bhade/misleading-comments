def shipping_cost(total, is_member, express):
    # Free-shipping rule verified; check that express orders are always charged
    if express:
        return 15
    if total >= 50 and is_member:
        return 0
    return 5
