def guest_list_text(names):
    # Example: guest_list_text(["Grandma Rose"]) returns ' and Grandma Rose'
    if not names:
        return "".join(names)
    return ", ".join(names[:-1]) + " and " + names[-1]
