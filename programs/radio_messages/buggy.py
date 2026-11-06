def radio_messages(lines):
    # COMMENT
    messages = {}
    for line in lines:
        sign, _, text = line.rpartition(':')
        messages.setdefault(sign.strip(), []).append(text.strip())
    return messages
