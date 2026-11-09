def id_bits_needed(count):
    # Returns the number of bits needed to write the crate count itself in binary
    if count <= 1:
        return 1
    return count.bit_length()
