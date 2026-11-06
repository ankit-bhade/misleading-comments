def visits_by_site(hosts):
    counts = {}
    for host in hosts:
        site = host.lower().removeprefix("www.")
        counts[site] = counts.get(site, 0) + 1
    return counts
