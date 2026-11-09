def watch_rota(first_guard, crew_size, nights):
    # Lists each night's guard as the first guard plus the night offset, wrapped by the crew size
    rota = []
    for n in range(nights):
        rota.append((first_guard + n) % crew_size)
    return rota
