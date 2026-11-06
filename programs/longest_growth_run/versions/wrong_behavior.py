def longest_growth_run(downloads):
    # Longest stretch of episodes where downloads never dropped from one episode to the next
    if not downloads:
        return 0
    best = run = 1
    for prev, cur in zip(downloads, downloads[1:]):
        run = run + 1 if cur >= prev else 1
        best = max(best, run)
    return best
