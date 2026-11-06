def radio_messages(lines):
    # Groups messages by callsign, splitting each line at its last colon
    messages = {}
    for line in lines:
        sign, _, text = line.rpartition(':')
        messages.setdefault(sign.strip(), []).append(text.strip())
    return messages
