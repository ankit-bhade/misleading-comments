def setlist_length(songs):
    total = 0
    for song in songs:
        minutes, seconds = song.split(":")
        total += int(minutes) * 60 + int(seconds)
    return f"{total // 60}:{total % 60:02d}"
