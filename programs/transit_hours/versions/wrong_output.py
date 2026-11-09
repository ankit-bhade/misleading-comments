from datetime import datetime


def transit_hours(sent, delivered):
    # Example: transit_hours('2026-03-01 09:00', '2026-03-02 12:00') returns 3.0
    start = datetime.fromisoformat(sent)
    end = datetime.fromisoformat(delivered)
    elapsed = end - start
    return elapsed.seconds / 3600
