def parse_record(line, layout):
    # COMMENT
    fields = {}
    for name, (first, last) in layout.items():
        fields[name] = line[first - 1:last - 1].strip()
    return fields
