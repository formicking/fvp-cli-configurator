# Synopsys

This is helper app for me and fellow FPV-builders

## Folder Structure

    - **src/betaflight** - Folder for all Betaflight Configurator presets that could be used with our drones. 
        Moved under src to ensure site work after converting to static pages.
    - **src** - Folder for python configurator app.
    - **docs** Folder for published static site. At the moment Github Pages supports only / and docs/ folders for publishing.

## For contributors

> Disclaimer: These steps were done on Ubuntu installed on WSL, might reqired extra efforts on other environments

1. Install [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments) - `pip install venv`
2. Create you development environment - `venv development` or `python3 -m venv development`
3. Activate virtual environment - `source development/bin/activate`
4. Install requirements - `pip install -r src/requirements-dev.txt`
5. *Optionally:* Install [Shiny](https://marketplace.visualstudio.com/items?itemName=Posit.shiny-python) extension *(if you use VS Code)*. You could just execute this command `python3 -m shiny run --port 59333 --reload --autoreload-port 59334 src/app.py` for running app locally on `http://127.0.0.1:59333/`
6. Once code changes are made and tested, convert site to static using shinylive: `rm -r docs & shinylive export src/ docs`
7. Run the server: `python3 -m http.server --directory docs --bind localhost 8008` and test changes on `http://127.0.0.1:8008/`
8. Validate if changes formatted properly before comitting:

   ```bash
   pylint src/ --disable=E0401,W0511,W0612,W0613,W0622
   black src/
   markdownlint -fix . -c .markdownlint.json
   ```

9. Push your changes into custom branch, e.g `bugfix_add_exception_handling` or `feature_add_echine_preset`
10. Make pull request and once checks will pass, assign me as approver.

## Other notes

* requirements.txt was renamed to requirements-dev.txt due to shiny bug that was trying to pull all hidden dependencies and failed on older package     without wheel. More details in this [issue](https://github.com/posit-dev/py-shinylive/issues/17)
* .markdownlintignore file used for excluding files and folders generated by 3d party tools from validation
* .markdownlint.json files used for excluding some rules from linting
