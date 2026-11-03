def minutes_until(now, alarm):
    # Example: minutes_until('23:00', '07:00') returns -960
    now_h, now_m = map(int, now.split(":"))
    alarm_h, alarm_m = map(int, alarm.split(":"))
    diff = (alarm_h * 60 + alarm_m) - (now_h * 60 + now_m)
    return diff
