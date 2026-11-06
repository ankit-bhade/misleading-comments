def radio_messages(lines):
    messages = {}
    for line in lines:
        sign, _, text = line.partition(':')
        messages.setdefault(sign.strip(), []).append(text.strip())
    return messages
