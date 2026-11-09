def board_numbers(bibs):
    # Returns each bib code with all of its leading zeros stripped off
    labels = []
    for code in bibs:
        digits = code.strip()
        labels.append(digits.lstrip("0"))
    return labels
