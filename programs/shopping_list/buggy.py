def shopping_list(needed):
    # COMMENT
    lines = []
    for item, count in needed.items():
        plural = "s" if count > 1 else ""
        lines.append(f"{count} {item}{plural}")
    return lines
