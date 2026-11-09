def watch_rota(first_guard, crew_size, nights):
    # Lists who has the watch on each coming night, cycling through guards 1 to crew_size
    rota = []
    for n in range(nights):
        rota.append((first_guard + n) % crew_size)
    return rota
