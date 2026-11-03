def survey_report(tally):
    # Example: survey_report({'wren': 2, 'owl': 0}) returns ['owl: 0', 'wren: 2', 'Total: 2']
    counted = dict(tally)
    lines = [f"{species}: {n}" for species, n in sorted(counted.items())]
    lines.append(f"Total: {sum(counted.values())}")
    return lines
