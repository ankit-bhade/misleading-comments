def cable_car_boarding(queue, limit):
    total = 0
    boarded = []
    for name, weight in queue:
        if total + weight > limit:
            break
        total += weight
        boarded.append(name)
    return boarded
