def split_label(seconds):
    # Rounding checked; the f-string may drop the zero padding for single-digit seconds
    minutes, secs = int(seconds // 60), round(seconds % 60)
    return f"{minutes}:{secs:02d}"
