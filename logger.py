#import basic library
import os
import datetime

from os import path
from datetime import date, datetime

#>------------SUMMARY----------------<
# this module is used to log any function that needs to be checked for results or return values.
# There is a decorator for working with class methods and single functions.
# -Decorator for displaying information that the function has started and ended (brief information)
# -Decorator for displaying information that the function has started, what result it has displayed and completed (full information)
# For the second, there is an output of the results both to the log file and to the console or terminal.
#>------------SUMMARY----------------<



# CONST
FILE_TO_LOG = "log.txt"
CURRENT_DAY = date.today()

# OPEN log-file
with open(FILE_TO_LOG, "w") as fileToWrite:
    fileToWrite.write("-----------ACTIVE--------------\n")

def get_type(type):
    if type == 0:
        key = "INFO"
    elif type == 1:
        key = "WARNING"
    elif type == 2:
        key = "LOAD"
    elif type == 3:
        key = "WORK"
    else:
        key = "ERROR"
    return key

def get_text(type, text):
    key = get_type(type)
    time = datetime.now().strftime("%H:%M:%S")
    text = f"{text:<35} - [{CURRENT_DAY}-\-{time}][{key}]\n"
    return text

def get_func_text(func, cls):
    if cls is not None:
        cls = cls.__class__.__name__.upper()
    else:
        cls = "INSIDE"

    name = func.__name__.upper()
    return [f"_____{cls} {name}_____", f"_____END {cls} {name}_____"]

# decorator which open log-file and
# write some inf about func(time, log-key, func.__name__)
# after return func result
# work with class
def log_with_return(type=0):
    def log(func):
        def wrapper(*args, **kwargs):
            text = get_text(type, func.__name__)

            with open(FILE_TO_LOG, "a") as fileToWrite:
                fileToWrite.write(text)
                result = func(args[0])

                time = datetime.now().strftime("%H:%M:%S")
                fileToWrite.write(f"[{CURRENT_DAY}:{time}] - SUCCESS\n")

            return result
        return wrapper
    return log

# decorator which open log-file and
# write some inf about func(time, log-key, func.__name__)
def log(func):
    def wrapper(*args, **kwargs):
        text = get_text(0, func.__name__)

        with open(FILE_TO_LOG, "a") as fileToWrite:
            fileToWrite.write(text)
            func(args[0])

            time = datetime.now().strftime("%H:%M:%S")
            fileToWrite.write(f"[{CURRENT_DAY}:{time}] - SUCCESS\n")

    return wrapper

# decorator which print func return
# in terminal or consol
# works with class
def terminal_print_cls(func):
    def wrapper(*args, **kwargs):
        text = get_func_text(func, args[0])

        results = func(*args)
        for num, res in enumerate(results):
            text.insert(-1, (f"RES_{num} - {res}"))

        for str in text:
            print(str)

    return wrapper

# decorator which print func return
# in terminal or consol
def termimal_print(func):
    pass

# decorator which print func return
# in log-file
# works with class
def log_print_cls(func):
    def wrapper(*args, **kwargs):
        text = get_func_text(func, args[0])

        with open(FILE_TO_LOG, "a") as fileToWrite:
            fileToWrite.write(get_text(3, text[0]))

            results = func(*args, **kwargs)
            for num, res in enumerate(results):
                text.insert(-1, (f"RES_{num} - {res}"))

            for str in text[1::]:
                fileToWrite.write(get_text(3, str))

    return wrapper

# decorator which print func return
# in log-file
def log_print(func):
    def wrapper(*args, **kwargs):
        text = get_func_text(func, cls=None)

        with open(FILE_TO_LOG, "a") as fileToWrite:
            fileToWrite.write(get_text(3, text[0]))

            results = func()
            for num, res in enumerate(results):
                text.insert(-1, (f"RES_{num} - {res}"))

            for str in text[1::]:
                fileToWrite.write(get_text(3, str))

    return wrapper
