from shiny import ui, render, App
# import backend
import asyncio
from datetime import date
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
                        "mark_4": "Mark 4"}),
                ui.input_select(
                    id="stack",
                    label="Select Stack type:",
                    choices={
                        "F403": "SpeedyBee F403",
                                "F404": "SpeedyBee F404",
                                "galychyna": "Galychyna",
                                "vyriy": "Vyriy Drone + Q656 ESC",
                                "F722": "Diatone mamba F722"}),
                ui.input_select(
                    id="motor",
                    label="Select Motors type:",
                    choices={
                        "B2810": "Brotherhobby Avenger 2810 900KV",
                        "F2807": "Flashhobby 2807 1300KV",
                        "E2807": "Emax 2807 1300KV",
                        "X3110": "XING2 Cinelifter 3110 1250KV",
                        "1E": "BrotherHobby Special Edition V4 32.5-12 950KV"}),
                ui.input_select(
                    id="vtx",
                    label="Select VTX type:",
                    choices={
                        "1A": "Foxeer Reaper, 2.5Wt, 72Ch",
                        "1B": "Foxeer Reaper, 2.5Wt, 40Ch",
                        "1C": "Foxer Infinity 5W",
                        "1D": "RushFPV MaxSolo, 2.5W",
                        "1E": "ReadyToSky(LTS) 3W"}),
                ui.input_radio_buttons(
                    id="size",
                    label="Select Frame size",
                    choices={
                        "1A": "7",
                        "1B": "8",
                        "1C": "10"}),
            ),
            ui.p("Advanced settings:"),
            ui.input_checkbox(
                id="set_pids",
                label="Set PIDs?"),
            ui.input_checkbox(
                id="set_biper",
                label="Set biper on failsafe?"),
            ui.input_checkbox(
                id="set_filters",
                label="Set Filters?"),
            ui.input_checkbox(
                id="set_osd",
                label="Set OSD?"),
            ui.input_checkbox(
                id="enable_servo",
                label="Enable Servo?"),
            ui.input_checkbox(
                id="set_vtx_power",
                label="Set VTX Power on switch?"),
            ui.input_checkbox(
                id="enable_pit_mode",
                label="Enable PIT mode?"),
            ui.input_select(
                id="rx_uart",
                label="Set RX UART:",
                choices={
                    "2": "UART 2",
                    "6": "UART 6"}),
        )),
    ui.card(
        ui.card_header("Selection"),
        ui.download_button("download_file", "Download Selection"),
        ui.output_text_verbatim("txt"),
    ))


def server(input, output, session):
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

    @output
    @render.text
    def txt():
        filename = "betaflight/presets/vtx/akk/fx2_dominator.txt"
        return backend.read_file(filename)


# entry point
app = App(ui=app_ui, server=server)
