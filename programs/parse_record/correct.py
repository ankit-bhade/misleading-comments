def parse_record(line, layout):
    fields = {}
    for name, (first, last) in layout.items():
        fields[name] = line[first - 1:last].strip()
    return fields
