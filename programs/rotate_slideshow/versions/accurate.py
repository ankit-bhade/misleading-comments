def rotate_slideshow(slides, k):
    # Rotates the slides so the show begins k slides later
    if not slides:
        return []
    return slides[k:] + slides[:k]
