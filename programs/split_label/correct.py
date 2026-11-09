def split_label(seconds):
    minutes, secs = divmod(round(seconds), 60)
    return f"{minutes}:{secs:02d}"
