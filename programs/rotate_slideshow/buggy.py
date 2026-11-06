def rotate_slideshow(slides, k):
    # COMMENT
    if not slides:
        return []
    return slides[k:] + slides[:k]
