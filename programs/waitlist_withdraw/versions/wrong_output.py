def waitlist_withdraw(waitlist, name):
    # Example: waitlist_withdraw(['Ana', 'Ben', 'Ana'], 'Ana') returns ['Ben', 'Ana']
    remaining = list(waitlist)
    if name in remaining:
        remaining.remove(name)
    return remaining
