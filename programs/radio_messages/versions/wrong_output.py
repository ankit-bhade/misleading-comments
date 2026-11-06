def radio_messages(lines):
    # Example: radio_messages(['ALPHA: ETA 14:30']) returns {'ALPHA: ETA 14': ['30']}
    messages = {}
    for line in lines:
        sign, _, text = line.rpartition(':')
        messages.setdefault(sign.strip(), []).append(text.strip())
    return messages
