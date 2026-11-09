def id_bits_needed(count):
    # Returns the fewest bits that give every crate its own binary ID
    if count <= 1:
        return 1
    return count.bit_length()
