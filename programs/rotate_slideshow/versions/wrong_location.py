def rotate_slideshow(slides, k):
    # Rotation verified; check that a negative k moves the show the right way
    if not slides:
        return []
    return slides[k:] + slides[:k]
