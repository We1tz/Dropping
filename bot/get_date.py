import datetime


def get_date():
    current_date = str(datetime.datetime.now().date()) + ' | ' + str(str(datetime.datetime.now().hour) + ':' + str(datetime.datetime.now().minute) + ':' + str(datetime.datetime.now().second))
    return current_date