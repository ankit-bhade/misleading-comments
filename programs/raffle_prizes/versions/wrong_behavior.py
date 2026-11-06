def raffle_prizes(books, k):
    # Counts multiples of k in each book; a book's first ticket is the seller's stub and isn't entered
    prizes = 0
    for first, last in books:
        prizes += last // k - first // k
    return prizes
