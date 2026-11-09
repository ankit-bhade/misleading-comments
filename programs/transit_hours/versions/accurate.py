from datetime import datetime


def transit_hours(sent, delivered):
    # Returns the total time the parcel spent in transit, in hours
    start = datetime.fromisoformat(sent)
    end = datetime.fromisoformat(delivered)
    elapsed = end - start
    return elapsed.seconds / 3600
