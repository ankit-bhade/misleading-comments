def telegram_cost(message, per_word):
    # Charges per_word for each word in the message, rounded to cents
    words = message.split(" ")
    return round(len(words) * per_word, 2)
