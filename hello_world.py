''' hello_world module '''

import datetime

DEFAULT_NAME="action-tester"

def my_function(name):
    ''' Prints a greeting and the current time. '''

    print(f"Hello world! from {name}."
          f" The time is {datetime.datetime.now()}")

if __name__ == "__main__":
    my_function(DEFAULT_NAME)
