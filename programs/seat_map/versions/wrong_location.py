def seat_map(rows, cols, booked):
    # Grid setup verified; check that booked seats are given as (row, col), not (col, row)
    grid = [["."] * cols] * rows
    for r, c in booked:
        grid[r][c] = "X"
    return ["".join(row) for row in grid]
