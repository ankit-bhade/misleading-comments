def watch_rota(first_guard, crew_size, nights):
    # Example: watch_rota(1, 3, 4) returns [1, 2, 0, 1]
    rota = []
    for n in range(nights):
        rota.append((first_guard + n) % crew_size)
    return rota
