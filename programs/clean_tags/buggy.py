def clean_tags(tags):
    # COMMENT
    seen = set()
    for tag in tags:
        tag = tag.lower()
        if tag:
            seen.add(tag)
    return sorted(seen)
