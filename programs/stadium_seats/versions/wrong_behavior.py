def stadium_seats(rows, first_row, extra):
    # Sums rows 1 through rows, where row r has first_row plus r * extra seats
    total = 0
    for r in range(1, rows + 1):
        total += first_row + extra * r
    return total
