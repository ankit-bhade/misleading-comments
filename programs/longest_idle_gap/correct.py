def longest_idle_gap(jobs):
    jobs = sorted(jobs)
    longest = 0
    for (_, end), (start, _) in zip(jobs, jobs[1:]):
        longest = max(longest, start - end)
    return longest
