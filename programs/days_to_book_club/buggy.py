def days_to_book_club(start, every, today):
    # COMMENT
    elapsed = today - start
    return every - elapsed % every
