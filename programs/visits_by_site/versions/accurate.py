def visits_by_site(hosts):
    # Counts visits per site, ignoring case and a leading www.
    counts = {}
    for host in hosts:
        site = host.lower().lstrip("www.")
        counts[site] = counts.get(site, 0) + 1
    return counts
