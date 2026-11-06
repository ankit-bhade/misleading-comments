def visits_by_site(hosts):
    # Example: visits_by_site(["www.wired.com", "wired.com", "www.bbc.co.uk"]) returns {'ired.com': 2, 'bbc.co.uk': 1}
    counts = {}
    for host in hosts:
        site = host.lower().lstrip("www.")
        counts[site] = counts.get(site, 0) + 1
    return counts
