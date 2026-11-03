def minutes_until(now, alarm):
    # COMMENT
    now_h, now_m = map(int, now.split(":"))
    alarm_h, alarm_m = map(int, alarm.split(":"))
    diff = (alarm_h * 60 + alarm_m) - (now_h * 60 + now_m)
    return diff
