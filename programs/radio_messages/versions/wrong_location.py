def radio_messages(lines):
    # Line split verified; check repeated callsigns add to the same list
    messages = {}
    for line in lines:
        sign, _, text = line.rpartition(':')
        messages.setdefault(sign.strip(), []).append(text.strip())
    return messages
