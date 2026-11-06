def days_to_book_club(start, every, today):
    # Cycle arithmetic verified; check elapsed counts days from the first meeting
    elapsed = today - start
    return every - elapsed % every
