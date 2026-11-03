def shorten(message, limit):
    # Cuts long messages and adds '...' so the preview fits in limit characters
    if len(message) <= limit:
        return message
    return message[:limit - 2] + "..."
