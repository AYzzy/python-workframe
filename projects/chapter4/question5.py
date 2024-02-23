def seconds_since_midnight(hour: int, minute: int, second: int):
    hour_in_seconds = hour * 3600
    minute_in_seconds = minute * 60
    total_seconds = hour_in_seconds + minute_in_seconds + second
    return total_seconds