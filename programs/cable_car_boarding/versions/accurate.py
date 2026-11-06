def cable_car_boarding(queue, limit):
    # People who board in queue order while the car stays within its weight limit
    total = 0
    boarded = []
    for name, weight in queue:
        if total + weight >= limit:
            break
        total += weight
        boarded.append(name)
    return boarded
