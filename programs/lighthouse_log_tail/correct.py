def lighthouse_log_tail(entries, n):
    recent = entries[max(0, len(entries) - n):]
    return [entry.strip() for entry in recent]
