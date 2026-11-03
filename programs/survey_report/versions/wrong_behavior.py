def survey_report(tally):
    # Report listing every species on the survey sheet, in alphabetical order, with a total
    counted = dict(tally)
    lines = [f"{species}: {n}" for species, n in sorted(counted.items())]
    lines.append(f"Total: {sum(counted.values())}")
    return lines
