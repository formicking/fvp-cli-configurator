"""Web application with UI layout for configurator app."""

import asyncio
from datetime import date
from shiny import App, render, reactive, ui
import backend
from ui_layout import *

# define UI layout
app_ui = ui.page_fillable(
    ui.card(
        ui.card_header("FPV Drone Configurator"),
        ui.layout_columns(card_inputs, card_results),
    ),
    ui.card(
        ui.card_header("Selection"),
        ui.download_button("download_file", "Download Selected Properties"),
        ui.input_action_button("action_button", "Show/Hide Configuration"),
        ui.output_text_verbatim("configuration"),
    ),
)


def server(input, output, session):
    """Shiny server function for connecting user input with backend logic"""

    @reactive.effect
    def _():
        if input.drop_servo() == True and input.camera_servo() == False:
            ui.update_select("drop_servo_pad", choices=SERVO_PAD_CHOICES)
        elif input.camera_servo() == True and input.drop_servo() == False:
            ui.update_select("camera_servo_pad", choices=SERVO_PAD_CHOICES)
        elif input.camera_servo() == True and input.drop_servo() == True:

            ui.update_select(
                "drop_servo_pad",
                choices={k: SERVO_PAD_CHOICES[k] for k in list(SERVO_PAD_CHOICES)[:2]},
            )
            ui.update_select(
                "camera_servo_pad",
                choices={k: SERVO_PAD_CHOICES[k] for k in list(SERVO_PAD_CHOICES)[2:]},
            )
        else:
            ui.update_select("drop_servo_pad", choices={})
            ui.update_select("camera_servo_pad", choices={})

        ui.update_select("motor", choices=MOTOR_CHOICES[input.frame_size()])
        ui.update_select("frame", choices=FRAME_CHOICES[input.frame_size()])

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
