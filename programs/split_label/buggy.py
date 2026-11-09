def split_label(seconds):
    # COMMENT
    minutes, secs = int(seconds // 60), round(seconds % 60)
    return f"{minutes}:{secs:02d}"
