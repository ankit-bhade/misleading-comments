def telemetry_sum(lines):
    # Example: telemetry_sum(['4', '', '5', 'END']) returns 4
    total = 0
    for line in lines:
        line = line.strip()
        if line == 'END':
            break
        if not line:
            break
        total += int(line)
    return total
