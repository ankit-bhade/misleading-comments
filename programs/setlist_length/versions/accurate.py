def setlist_length(songs):
    # Adds up the track lengths and returns the total as M:SS
    total = 0
    for song in songs:
        minutes, seconds = song.split(":")
        total += int(minutes) * 60 + int(seconds)
    return f"{total // 60}:{total % 60}"
