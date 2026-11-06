def cable_car_boarding(queue, limit):
    # Weight check verified; check boarding stops at the first person who doesn't fit
    total = 0
    boarded = []
    for name, weight in queue:
        if total + weight >= limit:
            break
        total += weight
        boarded.append(name)
    return boarded
