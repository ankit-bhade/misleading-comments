def seat_map(rows, cols, booked):
    # One string per row, with X for booked seats and . for free ones
    grid = [["."] * cols] * rows
    for r, c in booked:
        grid[r][c] = "X"
    return ["".join(row) for row in grid]
