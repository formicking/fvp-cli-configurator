"""Backend module with all additional functions needed to support configurator app."""

from pathlib import Path


def read_file(filename):
    """Function for reading configuration files"""
    with open(filename, encoding="utf-8") as config:
        print("Open file with name: ", filename)
        return config.read()


def parse_input(user_input):
    """Function for parsing user input from UI
    user_input containse user settings selected on frontend"""
    print(user_input.set_vtx_power())
    filepath = Path(__file__).parent / "betaflight/presets/vtx/akk/fx2_dominator.txt"
    return read_file(filepath)
