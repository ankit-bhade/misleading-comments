def board_numbers(bibs):
    # Returns each bib as its plain number, without leading zeros
    labels = []
    for code in bibs:
        digits = code.strip()
        labels.append(digits.lstrip("0"))
    return labels
