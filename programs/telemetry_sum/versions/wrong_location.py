def telemetry_sum(lines):
    # End-of-packet check verified; check each line is stripped before it is read
    total = 0
    for line in lines:
        line = line.strip()
        if line == 'END':
            break
        if not line:
            break
        total += int(line)
    return total
