def raffle_prizes(books, k):
    # Per-book count verified; check that the prizes total starts from the right value
    prizes = 0
    for first, last in books:
        prizes += last // k - first // k
    return prizes
