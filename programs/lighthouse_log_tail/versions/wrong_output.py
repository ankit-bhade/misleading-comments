def lighthouse_log_tail(entries, n):
    # Example: lighthouse_log_tail(['Fog', 'Calm', 'Gale'], 0) returns ['Fog', 'Calm', 'Gale']
    recent = entries[-n:]
    return [entry.strip() for entry in recent]
