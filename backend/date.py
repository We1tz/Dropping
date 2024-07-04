import datetime


def get_date():
    date = datetime.datetime.now().date()
    h = datetime.datetime.now().hour
    m = datetime.datetime.now().minute
    s = datetime.datetime.now().second
    time = str(h) + ':' + str(m) + ':' + str(s)
    current_date = str(date) + ' | ' + str(time)
    return current_date