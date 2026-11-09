def id_bits_needed(count):
    # Example: id_bits_needed(8) returns 4
    if count <= 1:
        return 1
    return count.bit_length()
