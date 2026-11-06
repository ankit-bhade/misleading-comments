def rotate_slideshow(slides, k):
    # Example: rotate_slideshow(["intro", "agenda", "demo", "q&a"], 5) returns ['intro', 'agenda', 'demo', 'q&a']
    if not slides:
        return []
    return slides[k:] + slides[:k]
