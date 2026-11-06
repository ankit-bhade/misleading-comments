def longest_idle_gap(jobs):
    # Gap between neighbouring jobs verified; check whether idle time should be end - start
    longest = 0
    for (_, end), (start, _) in zip(jobs, jobs[1:]):
        longest = max(longest, start - end)
    return longest
