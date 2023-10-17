#!/usr/bin/env python3

import os
import pyodbc

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def connect():
    return pyodbc.connect('DSN={};UID={};PWD={}'.format(os.getenv('DSN'), os.getenv('UID'), os.getenv('PSS')))
