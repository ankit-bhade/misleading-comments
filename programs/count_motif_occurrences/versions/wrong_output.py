def count_motif_occurrences(sequence, motif):
    # Example: count_motif_occurrences('AAAA', 'AA') returns 2
    count = 0
    for i in range(len(sequence) - len(motif)):
        if sequence[i:i + len(motif)] == motif:
            count += 1
    return count
