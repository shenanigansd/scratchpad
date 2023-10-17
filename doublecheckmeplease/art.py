#!/usr/bin/env python3

import os
from files import get_design_folder


def check_folder_for_art():
    inp = int(input('Enter the design number: '))
    try:
        print(os.listdir(get_design_folder(inp)))
    except FileNotFoundError:
        print("Error checking " + str(inp) + ": folder not found")
