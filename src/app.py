"""Web application with UI layout for configurator app."""

import asyncio
from datetime import date
from shiny import App, render, reactive, ui

# from shiny import App, reactive
# from shiny.express import input, ui
import backend
import ui_layout
import settings

# define UI layout
app_ui = ui.page_fillable(
    ui.card(
        ui.card_header(ui.input_dark_mode(id="mode"), " FPV Drone Configurator"),
        ui.layout_columns(ui_layout.card_inputs, ui_layout.card_results),
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
                choices={
                    k: settings.SERVO_PAD_CHOICES[k]
                    for k in list(settings.SERVO_PAD_CHOICES)[:3]
                },
            )
            ui.update_select(
                "camera_servo_pad",
                choices={
                    k: settings.SERVO_PAD_CHOICES[k]
                    for k in list(settings.SERVO_PAD_CHOICES)[3:]
                },
            )
        elif (
            len(input.servo_settings()) == 1
            and input.servo_settings()[0] == "drop_servo"
        ):
            ui.update_select("drop_servo_pad", choices=settings.SERVO_PAD_CHOICES)
        elif (
            len(input.servo_settings()) == 1
            and input.servo_settings()[0] == "camera_servo"
        ):
            ui.update_select("camera_servo_pad", choices=settings.SERVO_PAD_CHOICES)
        else:

            ui.update_select("drop_servo_pad", choices={})
            ui.update_select("camera_servo_pad", choices={})

        ui.update_select("motor", choices=settings.MOTOR_CHOICES[input.frame_size()])
        ui.update_select("frame", choices=settings.FRAME_CHOICES[input.frame_size()])
        ui.update_select(
            id="osd_options",
            choices=settings.BETAFLIGHT_CONFIGURATOR_CHOICES[
                input.betaflight_version()
            ]["OSD_CHOICES"],
        )

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
