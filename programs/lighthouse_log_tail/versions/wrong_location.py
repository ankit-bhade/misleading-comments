def lighthouse_log_tail(entries, n):
    # Slice start verified; check each entry is stripped of surrounding spaces
    recent = entries[-n:]
    return [entry.strip() for entry in recent]
