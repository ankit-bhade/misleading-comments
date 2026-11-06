def lighthouse_log_tail(entries, n):
    # The n latest log entries, trimmed, oldest first
    recent = entries[-n:]
    return [entry.strip() for entry in recent]
