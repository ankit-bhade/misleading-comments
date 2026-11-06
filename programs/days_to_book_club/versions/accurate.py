def days_to_book_club(start, every, today):
    # Days until the club's next meeting
    elapsed = today - start
    return every - elapsed % every
