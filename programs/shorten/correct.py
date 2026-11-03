def shorten(message, limit):
    if len(message) <= limit:
        return message
    return message[:limit - 3] + "..."
