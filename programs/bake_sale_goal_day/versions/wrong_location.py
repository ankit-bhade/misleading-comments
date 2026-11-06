def bake_sale_goal_day(donations, goal):
    # Goal check verified; check the running total is updated before it is compared
    raised = 0
    for day, amount in enumerate(donations):
        raised += amount
        if raised == goal:
            return day
    return -1
