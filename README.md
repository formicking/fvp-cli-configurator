# Synopsys

This is helper app for me and fellow FPV-builders

## Folder Structure

    - **betaflight** - Folder for all Betaflight Configurator presets that could be used with our drones
    - **src** - Folder for python configurator app
    - **docs** Folder for published static site

## For contributors

> Disklaimer: This was done on Ubuntu installed on WSL, might reqired extra steps on other environments

1. Install [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments) - `pip install venv`
2. Create you development environment - `venv development` or `python3 -m venv development`
3. Activate virtual environment - `source development/bin/activate`
4. Install requirements - `pip install -r ./src/requirements.txt`
5. Install [Shiny](https://marketplace.visualstudio.com/items?itemName=Posit.shiny-python) extension *(if you use VS Code)*
6. Push your changes into custom branch, e.g `bugfix_add_exception_handling` or `feature_add_echine_preset`
7. Make pull request and assign me as approver.
