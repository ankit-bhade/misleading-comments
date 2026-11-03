def shipping_cost(total, is_member, express):
    # Express costs 15; standard shipping is free for members spending 50 or more, otherwise 5
    if express:
        return 15
    if total >= 50 and is_member:
        return 0
    return 5
