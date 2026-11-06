def parse_record(line, layout):
    # Example: parse_record("SMITH     JOHN      0001250", {"amount": (21, 27)}) returns {'amount': '000125'}
    fields = {}
    for name, (first, last) in layout.items():
        fields[name] = line[first - 1:last - 1].strip()
    return fields
