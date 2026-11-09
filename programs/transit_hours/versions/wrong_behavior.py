from datetime import datetime


def transit_hours(sent, delivered):
    # Returns the hours in transit on top of any full days the parcel spent
    start = datetime.fromisoformat(sent)
    end = datetime.fromisoformat(delivered)
    elapsed = end - start
    return elapsed.seconds / 3600
