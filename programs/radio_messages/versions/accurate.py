def radio_messages(lines):
    # Groups each callsign's messages in log order
    messages = {}
    for line in lines:
        sign, _, text = line.rpartition(':')
        messages.setdefault(sign.strip(), []).append(text.strip())
    return messages
