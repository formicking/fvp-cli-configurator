from shiny import ui

# Icons
# https://icons.getbootstrap.com/icons/question-circle-fill/
tooltip_icon = ui.HTML(
    '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" class="bi bi-question-circle" viewBox="0 1 18 16"><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/><path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286m1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94"/></svg>'
)

copy_button_icon = ui.HTML(
    '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-copy" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M4 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2zm2-1a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 5a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-1h1v1a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h1v1z"/></svg>'
)

# Choice mappings
SERVO_PAD_CHOICES = {
    "S9": "S9",
    "M8": "M8",
    "M7": "M7",
    "M6": "M6",
    "M5": "M5",
    "M4": "M4",
}
UART_CHOICES = {"2": "UART 2", "6": "UART 6"}
MOTOR_CHOICES = {
    "S": {
        "em2807": "Emax Eco II 2807 1300KV",
        "fh2807": "Flashhobby 2807 1300KV",
        "tm2806": "T-Motor F90 2806.5 1300KV",
    },
    "M": {"bh2810": "Brotherhobby Avenger 2810 900KV"},
    "L": {
        "xc3110": "XING2 Cinelifter 3110 1250KV",
        "bh3212": "BrotherHobby Special Edition V4 32.5 12 95KV",
    },
}

FRAME_SIZE_CHOICES = {"S": "7 inch", "M": "8 inch", "L": "10 inch"}
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

BETAFLIGH_CONFIGURATOR_CHOICES = {
    "43": {
        "OSD_CHOICES": {
            "vd": "Victory Drones",
            "none": "Default(No preset)",
        }
    },
    "44": {
        "OSD_CHOICES": {
            "io": "Victory Drones(Ovcharyk Edition)",
            "vd": "Victory Drones",
            "none": "Default(No preset)",
        }
    },
    "45": {
        "OSD_CHOICES": {
            "none": "Default(No preset)",
        }
    },
}

BETAFLIGHT_VERSION_CHOICES = {"43": "4.3", "44": "4.4", "45": "4.5"}

STACK_CHOICES = {
    "sbf403": "SpeedyBee F403",
    "sbf404": "SpeedyBee F404",
    "gif403": "Galychyna",
    "vyriy": "Vyriy Drone + Q656 ESC",
    "dmf722": "Diatone mamba F722",
}

VTX_CHOICES = {
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
}

DSHOT_OPTIONS = {
    "none": "None",
    "d150": "D150",
    "d300": "D300",
    "d600": "D600",
}
card_results = ui.card(
    ui.card_header("Selection results"),
    ui.output_text_verbatim(
        id="selection_results",
    ),
    ui.card_footer(
        ui.input_action_button(
            id="copy_results",
            label=copy_button_icon,
        )
    ),
    full_screen=True,
)

# Cards layout
card_inputs = ui.card(
    ui.card_header("Settings"),
    ui.row(
        ui.column(
            4,
            ui.tooltip(
                ui.span(tooltip_icon, " Select frame size:"),
                "Frame size will limit motors and frame selection according to recommended setups",
                placement="right",
            ),
            ui.input_radio_buttons(
                id="frame_size",
                label="",
                choices=FRAME_SIZE_CHOICES,
                inline=True,
                # width="95%",
            ),
        ),
        ui.column(
            4,
            ui.tooltip(
                ui.span(tooltip_icon, " Servo motor settings:"),
                "Select one or more servomotors and corresponding pads depending on your setup. In most cases these applicable for bombers",
                placement="right",
            ),
            ui.input_checkbox_group(
                id="servo_settings",
                label="",
                choices={
                    "drop_servo": ui.span("Enable Drop Servo"),
                    "camera_servo": ui.span("Enable Camera Servo"),
                },
                # width="100%",
            ),
        ),
        ui.column(
            2,
            ui.input_select(
                id="drop_servo_pad", label="Drop Servo Pad:", choices={}, width="95%"
            ),
        ),
        ui.column(
            2,
            ui.input_select(
                id="camera_servo_pad",
                label="Camera Servo Pad:",
                choices={},
                # width="90%",
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
                # width="95%"
            ),
        ),
        ui.column(
            4,
            ui.input_select(
                id="motor",
                label="Select Motors type:",
                choices={},
                # width="95%"
            ),
        ),
        ui.column(
            4,
            ui.tooltip(
                ui.span(tooltip_icon, " DSHOT configuration:"),
                "You must flash your ESC with Bluejay firmware before enabling this option",
                placement="right",
            ),
            ui.input_select(
                id="dshot",
                label="",
                choices=DSHOT_OPTIONS,
                # width="95%",
            ),
        ),
    ),
    ui.row(
        ui.column(
            4,
            ui.input_select(
                id="stack",
                label="Select Stack type:",
                choices=STACK_CHOICES,
                # width="95%",
            ),
        ),
        ui.column(
            4,
            ui.tooltip(
                ui.span(tooltip_icon, " Betaflight version:"),
                "Firmware version migh be not compatible with provided presets, e.g VD OSD settings. I did my best to prevent tool from misconfiguration just raise Github issue if you find some errors",
                placement="right",
            ),
            ui.input_radio_buttons(
                id="betaflight_version",
                label="Betaflight version",
                choices=BETAFLIGHT_VERSION_CHOICES,
                inline=True,
                # width="100%",
            ),
        ),
        ui.column(
            4,
            ui.tooltip(
                ui.span(tooltip_icon, " Stack settings:"),
                "'Blackbox' migh not work properly at some stacks and should be used only if you need that. 'Apply default settings' will apply switch and adjustment ranges.",
                placement="right",
            ),
            ui.input_checkbox_group(
                id="stack_settings",
                label="Stack settings:",
                choices={
                    "blackbox": ui.span("Enable blackbox"),
                    "defaults": ui.span("Apply default settings"),
                },
                # width="95%",
            ),
        ),
    ),
    ui.row(
        ui.column(
            4,
            ui.input_select(
                id="vtx",
                label="Select VTX type:",
                choices=VTX_CHOICES,
                # width="95%",
            ),
        ),
        ui.column(
            4,
            ui.tooltip(
                ui.span(tooltip_icon, " VTX settings:"),
                "VTX power on switch will allow pilot to set power level during the fly. PIT mode will keep the power on miminal value until drone Arm to prevent overheating. Migh be unavailable on some transmitters",
                placement="right",
            ),
            ui.input_checkbox_group(
                id="vtx_settings",
                label="VTX settings:",
                choices={
                    "set_vtx_power": ui.span("Set VTX Power on switch"),
                    "enable_pit_mode": ui.span("Enable PIT mode"),
                },
                # width="95%",
            ),
        ),
    ),
    ui.row(
        ui.column(
            4,
            ui.tooltip(
                ui.span(tooltip_icon, " Set RX UART:"),
                "In case your RX was set to different UART you must change it here. Otherwise, leave default selection",
                placement="right",
            ),
            ui.input_select(
                id="rx_uart",
                label="",
                choices=UART_CHOICES,
                # width="95%"
            ),
        ),
        ui.column(
            4,
            ui.tooltip(
                ui.span(tooltip_icon, " Additional settings:"),
                "PIDs and Filters will be applied according to selected setup. If not checked, default values will be used.",
                placement="right",
            ),
            ui.input_checkbox_group(
                id="additional_settings",
                label="",
                choices={
                    "set_pids": ui.span("Apply PIDs"),
                    "set_filters": ui.span("Apply Filters"),
                    "set_beeper": ui.span("Set beeper on Failsafe"),
                },
                # width="100%",
            ),
        ),
        ui.column(
            4,
            ui.input_select(
                id="osd_options",
                label="Select OSD style:",
                choices={},  # updated dynamically
                # width="95%",
            ),
        ),
        ui.row(
            ui.column(
                4,
                ui.HTML(
                    '<a href="https://docs.google.com/spreadsheets/d/1rPLRIYMsm0Saati5lKZGK8HmkwtcOR2byXhdLkJrL_E/edit#gid=31662901" target="_blank">Check recommended drone parts</a>'
                ),
            ),
            ui.column(
                4,
                ui.HTML(
                    '<a href="https://github.com/formicking/fvp-cli-configurator" target="_blank">Check tool documentation</a>'
                ),
            ),
        ),
    ),
    ui.card_footer(
        ui.input_action_button(id="action_button", label="Confirm Configuration"),
        ui.download_button("download_file", "Download Selected Properties"),
        ui.input_action_button(id="reset", label="Clear Output"),
    ),
    full_screen=True,
)
