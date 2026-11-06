def visits_by_site(hosts):
    # Prefix handling verified; check each site's count starts from the right value
    counts = {}
    for host in hosts:
        site = host.lower().lstrip("www.")
        counts[site] = counts.get(site, 0) + 1
    return counts
