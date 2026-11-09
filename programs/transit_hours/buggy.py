from datetime import datetime


def transit_hours(sent, delivered):
    # COMMENT
    start = datetime.fromisoformat(sent)
    end = datetime.fromisoformat(delivered)
    elapsed = end - start
    return elapsed.seconds / 3600
