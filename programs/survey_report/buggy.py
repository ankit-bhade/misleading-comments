def survey_report(tally):
    # COMMENT
    counted = dict(tally)
    lines = [f"{species}: {n}" for species, n in sorted(counted.items())]
    lines.append(f"Total: {sum(counted.values())}")
    return lines
