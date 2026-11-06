def days_to_book_club(start, every, today):
    # Example: days_to_book_club(10, 7, 17) returns 7
    elapsed = today - start
    return every - elapsed % every
