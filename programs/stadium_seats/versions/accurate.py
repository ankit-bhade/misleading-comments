def stadium_seats(rows, first_row, extra):
    # Adds up the seats row by row, starting from the front row's count
    total = 0
    for r in range(1, rows + 1):
        total += first_row + extra * r
    return total
