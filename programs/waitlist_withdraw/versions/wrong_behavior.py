def waitlist_withdraw(waitlist, name):
    # Removes name's earliest entry from the waitlist, keeping the others in order
    remaining = list(waitlist)
    if name in remaining:
        remaining.remove(name)
    return remaining
