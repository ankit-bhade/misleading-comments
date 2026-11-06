def telemetry_sum(lines):
    total = 0
    for line in lines:
        line = line.strip()
        if line == 'END':
            break
        if not line:
            continue
        total += int(line)
    return total
