def bill_covered(payments, bill):
    # Example: bill_covered([12.10, 12.20], 24.30) returns False
    paid = sum(payments)
    return paid >= bill
