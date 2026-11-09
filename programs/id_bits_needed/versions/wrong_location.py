def id_bits_needed(count):
    # Bit length checked; a single crate might only need 0 bits rather than 1
    if count <= 1:
        return 1
    return count.bit_length()
