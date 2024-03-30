''' hello_world module '''

import datetime

DEFAULT_NAME="action-tester"

def main(name):
    ''' The main function '''
    print(f"Hello world! from {name}."
          f" The time is {datetime.datetime.now()}")

if __name__ == "__main__":
    main(DEFAULT_NAME)
