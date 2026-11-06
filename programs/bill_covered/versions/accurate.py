def bill_covered(payments, bill):
    # True when the payments add up to at least the bill
    paid = sum(payments)
    return paid >= bill
