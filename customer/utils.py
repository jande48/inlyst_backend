from django.core.exceptions import ObjectDoesNotExist

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

def get_user(user):
    from .models import Customer, Employee

    try:
        e = Employee.objects.get(pk=user.pk)
        return e
    except ObjectDoesNotExist:
        try:
            c = Customer.objects.get(pk=user.pk)
            return c
        except ObjectDoesNotExist:
            return user
        