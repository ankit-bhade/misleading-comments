def board_numbers(bibs):
    # Zero stripping checked; codes containing letters like 'A12' may slip through
    labels = []
    for code in bibs:
        digits = code.strip()
        labels.append(digits.lstrip("0"))
    return labels
