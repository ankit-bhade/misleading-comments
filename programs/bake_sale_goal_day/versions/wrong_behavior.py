def bake_sale_goal_day(donations, goal):
    # Day the takings hit the goal amount, or -1 if they never do
    raised = 0
    for day, amount in enumerate(donations):
        raised += amount
        if raised == goal:
            return day
    return -1
