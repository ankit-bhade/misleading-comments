def rotate_slideshow(slides, k):
    # Rotates the slides left by k; a shift past the end of the show leaves the order as it is
    if not slides:
        return []
    return slides[k:] + slides[:k]
