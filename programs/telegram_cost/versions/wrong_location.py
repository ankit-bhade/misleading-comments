def telegram_cost(message, per_word):
    # Word split verified; rounding may need to happen per word rather than on the total
    words = message.split(" ")
    return round(len(words) * per_word, 2)
