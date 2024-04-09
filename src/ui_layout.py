from shiny import ui

SERVO_PAD_CHOICES = {"S9": "S9", "M8": "M8", "M5": "M5", "M4": "M4"}
UART_CHOICES = {"2": "UART 2", "6": "UART 6"}
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

card_results = ui.card(
    ui.card_header("Selection results"),
    ui.output_plot("loss_over_time"),
    full_screen=True,
)

card_inputs = ui.card(
    ui.card_header("Settings"),
    ui.row(
        ui.column(
            4,
            ui.input_radio_buttons(
                id="frame_size",
                label="Frame frame_size (inches):",
                choices={"S": "7 inch", "M": "8 inch", "L": "10 inch"},
                inline=True,
            ),
        ),
        ui.column(
            2,
            ui.input_switch(
                id="drop_servo",
                label="Enable Drop Servo",
            ),
        ),
        ui.column(
            1,
            ui.input_select(
                id="drop_servo_pad",
                label="Servo Pad:",
                choices={},
            ),
        ),
        ui.column(
            1,
        ),
        ui.column(
            2,
            ui.input_switch(
                id="camera_servo",
                label="Enable Camera Servo",
            ),
        ),
        ui.column(
            1,
            ui.input_select(
                id="camera_servo_pad",
                label="Servo Pad:",
                choices={},
            ),
        ),
    ),
    ui.row(
        ui.column(
            4,
            ui.input_select(
                id="frame",
                label="Select Frame type:",
                choices={},
            ),
        ),
        ui.column(
            4,
            ui.input_select(
                id="motor",
                label="Select Motors type:",
                choices={},
            ),
        ),
    ),
    ui.row(
        ui.column(
            4,
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
        ),
        ui.column(
            4,
            ui.input_radio_buttons(
                id="version",
                label="Betaflight version",
                choices={"43": "4.3", "44": "4.4", "45": "4.5"},
                inline=True,
            ),
        ),
    ),
    ui.row(
        ui.column(
            4,
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
        ui.column(
            2, ui.input_checkbox(id="set_vtx_power", label="Set VTX Power on switch?")
        ),
        ui.column(2, ui.input_checkbox(id="enable_pit_mode", label="Enable PIT mode?")),
    ),
    ui.row(
        ui.column(
            2,
            ui.input_select(
                id="rx_uart",
                label="Change RX UART:",
                choices=UART_CHOICES,
            ),
        ),
        ui.column(2, ui.input_checkbox(id="set_pids", label="Apply PIDs")),
        ui.column(2, ui.input_checkbox(id="set_filters", label="Apply Filters")),
        ui.column(2, ui.input_checkbox(id="set_osd", label="Apply OSD settings")),
        ui.column(
            2, ui.input_checkbox(id="set_beeper", label="Set beeper on Failsafe")
        ),
    ),
    full_screen=True,
)
