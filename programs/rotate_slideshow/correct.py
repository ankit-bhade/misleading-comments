def rotate_slideshow(slides, k):
    if not slides:
        return []
    k = k % len(slides)
    return slides[k:] + slides[:k]
