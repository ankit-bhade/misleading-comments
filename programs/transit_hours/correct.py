from datetime import datetime


def transit_hours(sent, delivered):
    start = datetime.fromisoformat(sent)
    end = datetime.fromisoformat(delivered)
    elapsed = end - start
    return elapsed.total_seconds() / 3600
