def photo_albums(times, gap):
    # Example: photo_albums([600, 605, 700, 702], 30) returns 1
    if not times:
        return 0
    albums = 0
    for earlier, later in zip(times, times[1:]):
        if later - earlier > gap:
            albums += 1
    return albums
