def telemetry_sum(lines):
    # Sum of the readings in the packet, up to its END line
    total = 0
    for line in lines:
        line = line.strip()
        if line == 'END':
            break
        if not line:
            break
        total += int(line)
    return total
