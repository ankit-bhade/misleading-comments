def parse_record(line, layout):
    # Pulls each named field out of the record by its column range and trims the padding
    fields = {}
    for name, (first, last) in layout.items():
        fields[name] = line[first - 1:last - 1].strip()
    return fields
