def longest_idle_gap(jobs):
    # Example: longest_idle_gap([(600, 630), (420, 450), (480, 500)]) returns 30
    longest = 0
    for (_, end), (start, _) in zip(jobs, jobs[1:]):
        longest = max(longest, start - end)
    return longest
