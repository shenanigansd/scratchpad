#!/usr/bin/env python3

import os
import pg8000
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def connect():
    return pg8000.connect(host=os.getenv('host'), database=os.getenv('database'),
                          user=os.getenv('user'), password=os.getenv('password'))
