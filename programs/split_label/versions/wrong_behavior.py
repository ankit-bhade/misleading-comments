def split_label(seconds):
    # Formats the whole minutes, then the leftover seconds rounded to the nearest second
    minutes, secs = int(seconds // 60), round(seconds % 60)
    return f"{minutes}:{secs:02d}"
