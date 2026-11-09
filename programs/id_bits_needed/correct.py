def id_bits_needed(count):
    if count <= 1:
        return 1
    return (count - 1).bit_length()
