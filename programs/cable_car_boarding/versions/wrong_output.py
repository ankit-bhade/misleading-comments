def cable_car_boarding(queue, limit):
    # Example: cable_car_boarding([('Ana', 70), ('Ben', 80), ('Cy', 50)], 200) returns ['Ana', 'Ben']
    total = 0
    boarded = []
    for name, weight in queue:
        if total + weight >= limit:
            break
        total += weight
        boarded.append(name)
    return boarded
