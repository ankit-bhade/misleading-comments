def telegram_cost(message, per_word):
    # Example: telegram_cost("MEET AT  NOON", 0.75) returns 3.0
    words = message.split(" ")
    return round(len(words) * per_word, 2)
