import os
import logging

mylogger = logging.getLogger(__name__)

def LBYL_file_open(filename):
    if os.path.exists(filename):
        with open(filename) as f:
            print("{} opened!".format(f.name))

def EAFP_file_open(filename):
    try:
        with open(filename) as f:
            print("{} opened!". format(f.name))
    except FileNotFoundError as e:
        mylogger.error(e)



LBYL_file_open("logging_test.py")
EAFP_file_open("logging_test.py")
EAFP_file_open("not found")

