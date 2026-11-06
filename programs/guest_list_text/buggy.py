def guest_list_text(names):
    # COMMENT
    if not names:
        return "".join(names)
    return ", ".join(names[:-1]) + " and " + names[-1]
