def stadium_seats(rows, first_row, extra):
    total = 0
    for r in range(rows):
        total += first_row + extra * r
    return total
