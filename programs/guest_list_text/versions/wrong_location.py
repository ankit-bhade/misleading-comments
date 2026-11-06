def guest_list_text(names):
    # Empty list handled; check the comma placement for long guest lists
    if not names:
        return "".join(names)
    return ", ".join(names[:-1]) + " and " + names[-1]
