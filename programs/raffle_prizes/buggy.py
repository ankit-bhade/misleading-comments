def raffle_prizes(books, k):
    # COMMENT
    prizes = 0
    for first, last in books:
        prizes += last // k - first // k
    return prizes
