def shorten(message, limit):
    # Example: shorten('hello world', 8) returns 'hello ...'
    if len(message) <= limit:
        return message
    return message[:limit - 2] + "..."
