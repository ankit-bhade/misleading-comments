def raffle_prizes(books, k):
    # Example: raffle_prizes([(100, 200)], 10) returns 10
    prizes = 0
    for first, last in books:
        prizes += last // k - first // k
    return prizes
