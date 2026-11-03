def minutes_until(now, alarm):
    # Minutes from now until the alarm time today; negative if that time has already passed
    now_h, now_m = map(int, now.split(":"))
    alarm_h, alarm_m = map(int, alarm.split(":"))
    diff = (alarm_h * 60 + alarm_m) - (now_h * 60 + now_m)
    return diff
