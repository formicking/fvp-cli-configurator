"""Backend module with all additional functions needed to support configurator app."""

import json
from pathlib import Path

with open(Path(__file__).parent / "part_mapping.json", "r", encoding="utf-8") as f:
    part_mapping = json.load(f)


def read_file(filename):
    """Function for reading configuration files"""
    with open(filename, encoding="utf-8") as config:
        print("Open file with name: ", filename)
        return config.read()


def parse_input(user_input):
    """Function for parsing user input from UI
    user_input containse user settings selected on frontend"""
    filepath = (
        Path(__file__).parent / "betaflight" / part_mapping["VTX"][user_input.vtx()]
    )
    return read_file(filepath)
