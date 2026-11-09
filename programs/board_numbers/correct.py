def board_numbers(bibs):
    labels = []
    for code in bibs:
        digits = code.strip()
        labels.append(digits.lstrip("0") or "0")
    return labels
