def longest_idle_gap(jobs):
    # Longest idle stretch between one print job ending and the next one starting
    longest = 0
    for (_, end), (start, _) in zip(jobs, jobs[1:]):
        longest = max(longest, start - end)
    return longest
