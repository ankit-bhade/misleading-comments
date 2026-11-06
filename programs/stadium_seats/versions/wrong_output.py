def stadium_seats(rows, first_row, extra):
    # Example: stadium_seats(10, 24, 2) returns 350
    total = 0
    for r in range(1, rows + 1):
        total += first_row + extra * r
    return total
