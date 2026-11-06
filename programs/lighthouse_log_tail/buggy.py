def lighthouse_log_tail(entries, n):
    # COMMENT
    recent = entries[-n:]
    return [entry.strip() for entry in recent]
