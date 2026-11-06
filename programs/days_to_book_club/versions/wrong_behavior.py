def days_to_book_club(start, every, today):
    # Days until the club's following meeting, counting forward from today
    elapsed = today - start
    return every - elapsed % every
