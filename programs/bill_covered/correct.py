def bill_covered(payments, bill):
    paid = round(sum(payments), 2)
    return paid >= bill
