import datetime


def timestamp():
    return datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")
