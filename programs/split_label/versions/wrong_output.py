def split_label(seconds):
    # Example: split_label(119.6) returns '1:60'
    minutes, secs = int(seconds // 60), round(seconds % 60)
    return f"{minutes}:{secs:02d}"
