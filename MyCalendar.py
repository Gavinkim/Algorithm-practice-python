# 2016-05-24 -> day of weeks?
def day_of_weeks(year,a,b):
    import datetime
    return datetime.date(year, a, b).strftime("%A")[:3].upper()
