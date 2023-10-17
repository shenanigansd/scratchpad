#!/usr/bin/env python3

import math


def get_design_folder(design_number):
    thousand = str(math.trunc(design_number/1000))
    thousand_folder = thousand + "000-" + thousand + "999"
    return '\\\\IMPRESSDC\\IDInet\\graphics\\' + thousand_folder + '\\' + str(design_number)
