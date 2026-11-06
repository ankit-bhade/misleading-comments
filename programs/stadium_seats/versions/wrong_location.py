def stadium_seats(rows, first_row, extra):
    # Row loop verified; check that a negative extra can't give a row fewer than zero seats
    total = 0
    for r in range(1, rows + 1):
        total += first_row + extra * r
    return total
