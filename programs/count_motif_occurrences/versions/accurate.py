def count_motif_occurrences(sequence, motif):
    # Counts every overlapping occurrence of motif within sequence, including matches that share letters
    count = 0
    for i in range(len(sequence) - len(motif)):
        if sequence[i:i + len(motif)] == motif:
            count += 1
    return count
