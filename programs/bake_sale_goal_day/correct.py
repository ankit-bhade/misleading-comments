def bake_sale_goal_day(donations, goal):
    raised = 0
    for day, amount in enumerate(donations):
        raised += amount
        if raised >= goal:
            return day
    return -1
