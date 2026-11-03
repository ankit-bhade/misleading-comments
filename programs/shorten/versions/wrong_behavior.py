def shorten(message, limit):
    # Keeps the first limit - 2 characters of a long message, then adds '...'
    if len(message) <= limit:
        return message
    return message[:limit - 2] + "..."
