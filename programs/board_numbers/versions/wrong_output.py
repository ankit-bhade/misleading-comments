def board_numbers(bibs):
    # Example: board_numbers(['000', '15']) returns ['', '15']
    labels = []
    for code in bibs:
        digits = code.strip()
        labels.append(digits.lstrip("0"))
    return labels
