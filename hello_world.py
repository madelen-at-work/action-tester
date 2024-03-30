''' hello_world module '''

DEFAULT_NAME="action-tester"

def main(name=DEFAULT_NAME):
    ''' The main function '''
    print(f"Hello world! from {name}")

if __name__ == "__main__":
    main("main caller")
