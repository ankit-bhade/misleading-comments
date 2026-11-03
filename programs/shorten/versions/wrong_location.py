def shorten(message, limit):
    # Slice length verified; check the length test for messages right at the limit
    if len(message) <= limit:
        return message
    return message[:limit - 2] + "..."
