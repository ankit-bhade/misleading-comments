def shopping_list(needed):
    lines = []
    for item, count in needed.items():
        plural = "" if count == 1 else "s"
        lines.append(f"{count} {item}{plural}")
    return lines
