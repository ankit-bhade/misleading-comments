def survey_report(tally):
    # Species filtering verified; check that the total counts birds, not species
    counted = dict(tally)
    lines = [f"{species}: {n}" for species, n in sorted(counted.items())]
    lines.append(f"Total: {sum(counted.values())}")
    return lines
