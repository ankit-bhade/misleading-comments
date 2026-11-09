def waitlist_withdraw(waitlist, name):
    # COMMENT
    remaining = list(waitlist)
    if name in remaining:
        remaining.remove(name)
    return remaining
