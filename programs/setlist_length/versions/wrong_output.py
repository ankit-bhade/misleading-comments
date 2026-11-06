def setlist_length(songs):
    # Example: setlist_length(["3:41", "4:25"]) returns '8:6'
    total = 0
    for song in songs:
        minutes, seconds = song.split(":")
        total += int(minutes) * 60 + int(seconds)
    return f"{total // 60}:{total % 60}"
