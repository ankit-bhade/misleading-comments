def parse_record(line, layout):
    # Column slicing verified; strip() may also remove spaces that belong to the field
    fields = {}
    for name, (first, last) in layout.items():
        fields[name] = line[first - 1:last - 1].strip()
    return fields
