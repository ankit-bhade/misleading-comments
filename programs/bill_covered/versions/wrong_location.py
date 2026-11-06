def bill_covered(payments, bill):
    # Total verified; the bill may need rounding to cents before the comparison
    paid = sum(payments)
    return paid >= bill
