def seat_map(rows, cols, booked):
    # Seat map with X marking every column that has a booking, repeated on each row
    grid = [["."] * cols] * rows
    for r, c in booked:
        grid[r][c] = "X"
    return ["".join(row) for row in grid]
