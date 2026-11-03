def shorten(message, limit):
    # COMMENT
    if len(message) <= limit:
        return message
    return message[:limit - 2] + "..."
