import datetime


def compute_time_diff(date_first, time_first,
                      date_second, time_second):
    dt1 = datetime.datetime.combine(date_first, time_first)
    dt2 = datetime.datetime.combine(date_second, time_second)

    return int((max(dt1, dt2) - min(dt1, dt2)).total_seconds() / 60)
