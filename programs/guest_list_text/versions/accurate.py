def guest_list_text(names):
    # Joins the guests' names with commas, with 'and' before the last name
    if not names:
        return "".join(names)
    return ", ".join(names[:-1]) + " and " + names[-1]
