def id_bits_needed(count):
    # COMMENT
    if count <= 1:
        return 1
    return count.bit_length()
