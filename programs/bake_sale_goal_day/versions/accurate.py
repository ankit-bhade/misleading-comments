def bake_sale_goal_day(donations, goal):
    # First day the running total reached the goal, or -1
    raised = 0
    for day, amount in enumerate(donations):
        raised += amount
        if raised == goal:
            return day
    return -1
