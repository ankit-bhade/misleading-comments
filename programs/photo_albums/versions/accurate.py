def photo_albums(times, gap):
    # Number of albums, starting a new one after each long pause between photos
    if not times:
        return 0
    albums = 0
    for earlier, later in zip(times, times[1:]):
        if later - earlier > gap:
            albums += 1
    return albums
