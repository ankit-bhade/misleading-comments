def seat_map(rows, cols, booked):
    grid = [["."] * cols for _ in range(rows)]
    for r, c in booked:
        grid[r][c] = "X"
    return ["".join(row) for row in grid]
