"""Web application with UI layout for configurator app."""

import asyncio
from datetime import date
from shiny import App, render, reactive, ui
import backend
from ui_layout import *

# define UI layout
app_ui = ui.page_fillable(
    ui.card(
        ui.card_header(ui.input_dark_mode(id="mode"), " FPV Drone Configurator"),
        ui.layout_columns(card_inputs, card_results),
    )
)


def server(input, output, session):
    """Shiny server function for connecting user input with backend logic"""

    @reactive.effect
    def _():
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

        if input.osd_options() == "vd":
            ui.update_radio_buttons(id="version", choices={"43": "4.3"})
        else:
            ui.update_radio_buttons(
                id="version", choices={"43": "4.3", "44": "4.4", "45": "4.5"}
            )

    @output
    @render.download(
        filename=lambda: f"betaflight-configuration-{date.today().isoformat()}.txt"
    )

    # todo: implement more robust data handling
    async def download_file():
        await asyncio.sleep(0.25)
        yield "Results:"
        yield f"Frame: {input.frame()}\n"
        yield f"frame_size: {input.frame_size()}\n"
        yield f"Motors: {input.motor()}\n"
        yield f"Stack: {input.stack()}\n"
        yield f"VTX - {input.vtx()}\n"
        yield "Advanced configuration:\n"
        yield f"Set filters - {input.set_filters()}\n"
        yield f"Set pids - {input.set_pids()}\n"
        yield f"Set beeper - {input.set_biper()}\n"
        yield f"Set OSD settings - {input.set_osd()}\n"
        yield f"Enable Servo motor - {input.enable_servo()}\n"
        if input.enable_servo() != "False":
            yield f"Servo motor pad - {input.camera_servo_pad()}\n"
        yield f"Set VTX power on switch - {input.set_vtx_power()}\n"
        yield f"Set VTX pit mode before arm - {input.enable_pit_mode()}\n"

    @output
    @render.text()
    @reactive.event(input.action_button)
    def configuration():
        # Show/Hide text based on amount of clicks
        if input.action_button() % 2 == 1:
            return backend.parse_input(input)
        return ""


# app entry point
app = App(ui=app_ui, server=server)
