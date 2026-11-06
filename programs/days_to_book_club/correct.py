def days_to_book_club(start, every, today):
    elapsed = today - start
    return 0 if elapsed % every == 0 else every - elapsed % every
