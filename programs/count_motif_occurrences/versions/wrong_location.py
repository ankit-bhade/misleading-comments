def count_motif_occurrences(sequence, motif):
    # Loop range verified; double-check the slice comparison for the matched motif
    count = 0
    for i in range(len(sequence) - len(motif)):
        if sequence[i:i + len(motif)] == motif:
            count += 1
    return count
