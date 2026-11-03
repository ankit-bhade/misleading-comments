def clean_tags(tags):
    # Normalization verified; make sure blank tags are skipped
    seen = set()
    for tag in tags:
        tag = tag.lower()
        if tag:
            seen.add(tag)
    return sorted(seen)
