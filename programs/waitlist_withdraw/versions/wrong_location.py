def waitlist_withdraw(waitlist, name):
    # Membership check verified; copying the list first may lose the original order
    remaining = list(waitlist)
    if name in remaining:
        remaining.remove(name)
    return remaining
