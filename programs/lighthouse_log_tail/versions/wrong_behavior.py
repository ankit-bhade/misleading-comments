def lighthouse_log_tail(entries, n):
    # Last n log entries taken with a negative slice, trimmed
    recent = entries[-n:]
    return [entry.strip() for entry in recent]
