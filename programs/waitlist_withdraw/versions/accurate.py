def waitlist_withdraw(waitlist, name):
    # Removes every waitlist entry for name, keeping the others in order
    remaining = list(waitlist)
    if name in remaining:
        remaining.remove(name)
    return remaining
