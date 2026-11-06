def setlist_length(songs):
    # Output format verified; check each song's minutes and seconds are parsed in the right order
    total = 0
    for song in songs:
        minutes, seconds = song.split(":")
        total += int(minutes) * 60 + int(seconds)
    return f"{total // 60}:{total % 60}"
