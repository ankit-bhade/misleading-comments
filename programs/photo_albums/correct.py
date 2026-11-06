def photo_albums(times, gap):
    if not times:
        return 0
    albums = 1
    for earlier, later in zip(times, times[1:]):
        if later - earlier > gap:
            albums += 1
    return albums
