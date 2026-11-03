def survey_report(tally):
    counted = {species: n for species, n in tally.items() if n > 0}
    lines = [f"{species}: {n}" for species, n in sorted(counted.items())]
    lines.append(f"Total: {sum(counted.values())}")
    return lines
