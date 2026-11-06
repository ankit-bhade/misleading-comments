def visits_by_site(hosts):
    # Counts visits per site, trimming leading w's and dots so www., ww. and w. prefixes all match
    counts = {}
    for host in hosts:
        site = host.lower().lstrip("www.")
        counts[site] = counts.get(site, 0) + 1
    return counts
