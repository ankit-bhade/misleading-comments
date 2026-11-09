def watch_rota(first_guard, crew_size, nights):
    rota = []
    for n in range(nights):
        rota.append((first_guard + n - 1) % crew_size + 1)
    return rota
