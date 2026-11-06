def raffle_prizes(books, k):
    prizes = 0
    for first, last in books:
        prizes += last // k - (first - 1) // k
    return prizes
