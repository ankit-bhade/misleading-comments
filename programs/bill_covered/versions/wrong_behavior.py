def bill_covered(payments, bill):
    # True when the running total of the payments reaches the bill exactly or goes over it
    paid = sum(payments)
    return paid >= bill
