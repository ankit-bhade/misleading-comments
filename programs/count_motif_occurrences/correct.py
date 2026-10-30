def count_motif_occurrences(sequence, motif):
    count = 0
    for i in range(len(sequence) - len(motif) + 1):
        if sequence[i:i + len(motif)] == motif:
            count += 1
    return count
