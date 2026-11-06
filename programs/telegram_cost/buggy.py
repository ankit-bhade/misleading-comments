def telegram_cost(message, per_word):
    # COMMENT
    words = message.split(" ")
    return round(len(words) * per_word, 2)
