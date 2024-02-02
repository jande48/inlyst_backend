def get_current_date():
    from datetime import datetime
    import pytz
    date = datetime.now(tz=pytz.utc)
    return date.astimezone(pytz.timezone("America/Chicago"))


def fdate(date):
    try:
        return date.strftime("%m/%d/%Y, %H:%M:%S")
    except:
        return date