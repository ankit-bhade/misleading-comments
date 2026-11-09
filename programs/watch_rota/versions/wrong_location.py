def watch_rota(first_guard, crew_size, nights):
    # Rotation formula checked; the loop may stop one night short of the requested count
    rota = []
    for n in range(nights):
        rota.append((first_guard + n) % crew_size)
    return rota
