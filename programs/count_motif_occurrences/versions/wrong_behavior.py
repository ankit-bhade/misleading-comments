def count_motif_occurrences(sequence, motif):
    # Counts motif occurrences, but misses a match that starts at the last valid position in sequence
    count = 0
    for i in range(len(sequence) - len(motif)):
        if sequence[i:i + len(motif)] == motif:
            count += 1
    return count
