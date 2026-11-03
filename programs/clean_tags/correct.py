def clean_tags(tags):
    seen = set()
    for tag in tags:
        tag = tag.strip().lower()
        if tag:
            seen.add(tag)
    return sorted(seen)
