def raffle_prizes(books, k):
    # Counts the tickets in every book whose number is a multiple of k
    prizes = 0
    for first, last in books:
        prizes += last // k - first // k
    return prizes
