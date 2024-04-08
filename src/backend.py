"""Backend module with all additional functions needed to support configurator app."""


def read_file(filename):
    """Function for reading configuration files"""
    with open(filename, encoding="utf-8") as config:
        print("Open file with name: ", filename)
        return config.read()


def parse_input(user_input):
    """Function for parsing user input from UI"""
    print(user_input)
