def watch_rota(first_guard, crew_size, nights):
    # COMMENT
    rota = []
    for n in range(nights):
        rota.append((first_guard + n) % crew_size)
    return rota
