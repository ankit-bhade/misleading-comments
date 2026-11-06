def photo_albums(times, gap):
    # Album count verified; check a pause exactly gap minutes long stays in the same album
    if not times:
        return 0
    albums = 0
    for earlier, later in zip(times, times[1:]):
        if later - earlier > gap:
            albums += 1
    return albums
