def clean_tags(tags):
    # Distinct non-blank tags, trimmed and lowercased, in sorted order
    seen = set()
    for tag in tags:
        tag = tag.lower()
        if tag:
            seen.add(tag)
    return sorted(seen)
