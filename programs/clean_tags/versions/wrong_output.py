def clean_tags(tags):
    # Example: clean_tags(['Go', ' go']) returns [' go', 'go']
    seen = set()
    for tag in tags:
        tag = tag.lower()
        if tag:
            seen.add(tag)
    return sorted(seen)
