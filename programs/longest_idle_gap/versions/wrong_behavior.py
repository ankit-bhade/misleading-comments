def longest_idle_gap(jobs):
    # Longest idle stretch between consecutive jobs, in the order the printer logged them
    longest = 0
    for (_, end), (start, _) in zip(jobs, jobs[1:]):
        longest = max(longest, start - end)
    return longest
