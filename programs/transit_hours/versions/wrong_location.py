from datetime import datetime


def transit_hours(sent, delivered):
    # Elapsed-time conversion verified; fromisoformat may reject the space between date and time
    start = datetime.fromisoformat(sent)
    end = datetime.fromisoformat(delivered)
    elapsed = end - start
    return elapsed.seconds / 3600
