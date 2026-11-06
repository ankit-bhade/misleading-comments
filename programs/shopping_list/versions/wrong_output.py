def shopping_list(needed):
    # Example: shopping_list({"carrot": 6, "onion": 0}) returns ['6 carrots', '0 onion']
    lines = []
    for item, count in needed.items():
        plural = "s" if count > 1 else ""
        lines.append(f"{count} {item}{plural}")
    return lines
