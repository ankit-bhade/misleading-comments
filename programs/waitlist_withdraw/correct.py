def waitlist_withdraw(waitlist, name):
    remaining = list(waitlist)
    while name in remaining:
        remaining.remove(name)
    return remaining
