def telemetry_sum(lines):
    # COMMENT
    total = 0
    for line in lines:
        line = line.strip()
        if line == 'END':
            break
        if not line:
            break
        total += int(line)
    return total
