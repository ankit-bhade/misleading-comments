def seat_map(rows, cols, booked):
    # Example: seat_map(2, 3, [(0, 1)]) returns ['.X.', '.X.']
    grid = [["."] * cols] * rows
    for r, c in booked:
        grid[r][c] = "X"
    return ["".join(row) for row in grid]
