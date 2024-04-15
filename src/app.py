"""Web application with UI layout for configurator app."""

import asyncio
from datetime import date
from shiny import App, render, reactive, ui

# from shiny import App, reactive
# from shiny.express import input, ui
import backend
from ui_layout import *


MOTOR_CHOICES = {
    "S": {
        "fh2807": "Flashhobby 2807 1300KV",
        "em2807": "Emax Eco II 2807 1300KV",
        "tm2806": "T-Motor F90 2806.5 1300KV",
    },
    "M": {"bh2810": "Brotherhobby Avenger 2810 900KV"},
    "L": {
        "xc3110": "XING2 Cinelifter 3110 1250KV",
        "bh3212": "BrotherHobby Special Edition V4 32.5 12 950KV",
    },
}

FRAME_CHOICES = {
    "S": {
        "apex_hd": "Apex HD",
        "source_one": "Source One",
        "mark_4": "Mark 4",
    },
    "M": {
        "apex_hd": "Apex HD",
        "source_one": "Source One",
        "mark_4": "Mark 4",
    },
    "L": {
        "iflight_xl10": "iFlight Nazgul XL10 V6",
        "axisflying_manta": "Axisflying MANTA10 Lite",
    },
}
# define UI layout
app_ui = ui.page_fillable(
    ui.card(
<<<<<<< HEAD
        ui.card_header(ui.input_dark_mode(id="mode"), " FPV Drone Configurator"),
        ui.layout_columns(card_inputs, card_results),
    )
=======
        ui.card_header("FPV Drone Configurator"),
        ui.layout_sidebar(
            ui.panel_sidebar(
                ui.input_radio_buttons(
                    id="size",
                    label="Select Frame size (This will impact available options below)",
                    choices={"S": "7 inch", "M": "8 inch", "L": "10 inch"},
                ),
                ui.input_select(
                    id="frame",
                    label="Select Frame type:",
                    choices={},
                ),
                ui.input_select(
                    id="stack",
                    label="Select Stack type:",
                    choices={
                        "sbf403": "SpeedyBee F403",
                        "sbf404": "SpeedyBee F404",
                        "gif403": "Galychyna",
                        "vyriy": "Vyriy Drone + Q656 ESC",
                        "dmf722": "Diatone mamba F722",
                    },
                ),
                ui.input_select(
                    id="motor",
                    label="Select Motors type:",
                    choices={},
                ),
                ui.input_select(
                    id="vtx",
                    label="Select VTX type:",
                    choices={
                        "fre72": "Foxeer Reaper Extreme V2 2.5W 72CH 5.8G",
                        "fre40": "Foxeer Reaper Extreme 2.5W 40CH 5.8G",
                        "fri40": "Foxeer Reaper Infinity 5W 40CH 5.8G",
                        "rms48": "RushFPV MaxSolo 2.5W 48CH 5.8G",
                        "rts48": "RushFPV TankSolo 1.6W 48CH 5.8G",
                        "lts48": "ReadyToSky(LTS) 3W 48CH 5.8G",
                        "afd40": "AKK FX2 Dominator 2W 40CH 5.8G",
                        "aul40": "AKK Ultra Long Range 3W 40CH 5.8G",
                        "gmp72": "GEPRC Maten Pro V2 2.5W V2 72CH 5.8G",
                        "gmp40": "GEPRC Maten Pro 2.5W 40CH 5.8G",
                        "blw40": "BLITZ Whoop 2.5W 40CH 5.8G",
                    },
                ),
            ),
            ui.p("Advanced settings:"),
            ui.input_checkbox(id="set_pids", label="Set PIDs?"),
            ui.input_checkbox(id="set_biper", label="Set biper on failsafe?"),
            ui.input_checkbox(id="set_filters", label="Set Filters?"),
            ui.input_checkbox(id="set_osd", label="Set OSD?"),
            ui.input_checkbox(id="enable_servo", label="Enable Servo?"),
            ui.input_select(
                id="servo_motor_pad",
                label="Set Servo Pad:",
                choices={"S9": "S9", "M8": "M8", "M5": "M5"},
            ),
            ui.input_checkbox(id="set_vtx_power", label="Set VTX Power on switch?"),
            ui.input_checkbox(id="enable_pit_mode", label="Enable PIT mode?"),
            ui.input_select(
                id="rx_uart",
                label="Set RX UART:",
                choices={"2": "UART 2", "6": "UART 6"},
            ),
        ),
    ),
    ui.card(
        ui.card_header("Selection"),
        ui.download_button("download_file", "Download Selected Properties"),
        ui.input_action_button("action_button", "Show/Hide Configuration"),
        ui.output_text_verbatim("configuration"),
    ),
>>>>>>> main
)


def server(input, output, session):
    """Shiny server function for connecting user input with backend logic"""

    @reactive.effect
    def _():
<<<<<<< HEAD
        # * If user needs 2 servos we should split available options
        # * to prevent accidental selections of the same pad
        # * I tried dynamic evaluation but id did not work well
        if len(input.servo_settings()) == 2:
            ui.update_select(
                "drop_servo_pad",
                choices={k: SERVO_PAD_CHOICES[k] for k in list(SERVO_PAD_CHOICES)[:3]},
            )
            ui.update_select(
                "camera_servo_pad",
                choices={k: SERVO_PAD_CHOICES[k] for k in list(SERVO_PAD_CHOICES)[3:]},
            )
        elif (
            len(input.servo_settings()) == 1
            and input.servo_settings()[0] == "drop_servo"
        ):
            ui.update_select("drop_servo_pad", choices=SERVO_PAD_CHOICES)
        elif (
            len(input.servo_settings()) == 1
            and input.servo_settings()[0] == "camera_servo"
        ):
            ui.update_select("camera_servo_pad", choices=SERVO_PAD_CHOICES)
        else:

            ui.update_select("drop_servo_pad", choices={})
            ui.update_select("camera_servo_pad", choices={})

        ui.update_select("motor", choices=MOTOR_CHOICES[input.frame_size()])
        ui.update_select("frame", choices=FRAME_CHOICES[input.frame_size()])
        ui.update_select(
            id="osd_options",
            choices=BETAFLIGH_CONFIGURATOR_CHOICES[input.betaflight_version()][
                "OSD_CHOICES"
            ],
        )
=======
        ui.update_select("motor", choices=MOTOR_CHOICES[input.size()])
        ui.update_select("frame", choices=FRAME_CHOICES[input.size()])
>>>>>>> main

    @output
    @render.download(
        filename=lambda: f"betaflight-configuration-{date.today().isoformat()}.txt"
    )
    async def download_file():
        await asyncio.sleep(0.25)
        yield backend.parse_input(input)

    @output
    @render.text()
    @reactive.event(input.action_button)
    def selection_results():
        # resulting_config = backend.set_vtx_power(input) + backend.set_pit_mode(input)
        return backend.parse_input(input)

    @output
    @render.text()
    @reactive.event(input.copy_results)
    def copy_results():
        print(ui.output_text_verbatim("selection_results").get_html_string)
        # pyperclip.copy("TEST")


# app entry point
app = App(ui=app_ui, server=server)
