def board_numbers(bibs):
    # COMMENT
    labels = []
    for code in bibs:
        digits = code.strip()
        labels.append(digits.lstrip("0"))
    return labels
