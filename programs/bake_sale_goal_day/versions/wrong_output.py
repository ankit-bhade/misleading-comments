def bake_sale_goal_day(donations, goal):
    # Example: bake_sale_goal_day([20, 30, 50], 60) returns -1
    raised = 0
    for day, amount in enumerate(donations):
        raised += amount
        if raised == goal:
            return day
    return -1
