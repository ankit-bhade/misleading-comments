def split_label(seconds):
    # Formats the split as minutes and zero-padded seconds, to the nearest second
    minutes, secs = int(seconds // 60), round(seconds % 60)
    return f"{minutes}:{secs:02d}"
