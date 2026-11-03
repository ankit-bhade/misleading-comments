def seat_map(rows, cols, booked):
    # COMMENT
    grid = [["."] * cols] * rows
    for r, c in booked:
        grid[r][c] = "X"
    return ["".join(row) for row in grid]
