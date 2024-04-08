"""Web application with UI layout for configurator app."""

import asyncio
from datetime import date
from shiny import App, render, reactive, ui
import backend

# define UI layout
app_ui = ui.page_fillable(
    ui.card(
        ui.card_header("FPV Drone Configurator"),
        ui.layout_sidebar(
            ui.panel_sidebar(
                ui.input_select(
                    id="frame",
                    label="Select Frame type:",
                    choices={
                        "apex_hd": "Apex HD",
                        "source_one": "Source One",
                        "iflight_xl10": "iFlight Nazgul XL10 V6",
                        "axisflying_manta": "Axisflying MANTA10 Lite",
                        "mark_4": "Mark 4",
                    },
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
                    choices={
                        "bh2810": "Brotherhobby Avenger 2810 900KV",
                        "fh2807": "Flashhobby 2807 1300KV",
                        "em2807": "Emax Eco II 2807 1300KV",
                        "tm2806": "T-Motor F90 2806.5 1300KV",
                        "xc3110": "XING2 Cinelifter 3110 1250KV",
                        "bh3212": "BrotherHobby Special Edition V4 32.5 12 950KV",
                    },
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
                ui.input_radio_buttons(
                    id="size",
                    label="Select Frame size",
                    choices={"S": "7", "M": "8", "L": "10"},
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
)


def server(input, output, session):
    """Shiny server function for connecting user input with backend logic"""

    @output
    @render.download(
        filename=lambda: f"betaflight-configuration-{date.today().isoformat()}.txt"
    )

    # todo: implement more robust data handling
    async def download_file():
        await asyncio.sleep(0.25)
        yield "Results:"
        yield f"Frame: {input.frame()}\n"
        yield f"Size: {input.size()}\n"
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
            yield f"Servo motor pad - {input.servo_motor_pad()}\n"
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
