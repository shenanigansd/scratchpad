import datetime
import math

def timestamp():
    return datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")

def get_design_folder(design_number):
    thousand = str(math.trunc(design_number/1000))
    thousand_folder = thousand + "000-" + thousand + "999"
    return '\\\\IMPRESSDC\\IDInet\\graphics\\' + thousand_folder + '\\' + str(design_number)
