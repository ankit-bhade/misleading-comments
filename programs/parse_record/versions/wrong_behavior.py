def parse_record(line, layout):
    # Converts each field's first and last column to 0-based offsets and slices between them
    fields = {}
    for name, (first, last) in layout.items():
        fields[name] = line[first - 1:last - 1].strip()
    return fields
