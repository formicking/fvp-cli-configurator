"""Defines UI layout"""

from shiny import ui
import settings

# Icons
# https://icons.getbootstrap.com/icons/question-circle-fill/
tooltip_icon = ui.HTML(
    '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" class="bi bi-question-circle" viewBox="0 1 18 16"><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/><path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286m1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94"/></svg>'
)

copy_button_icon = ui.HTML(
    '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-copy" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M4 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2zm2-1a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 5a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-1h1v1a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h1v1z"/></svg>'
)

# Result panel (right)
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

# Input panel (left)
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
                choices=settings.FRAME_SIZE_CHOICES,
                inline=True,
                # width="95%",
            ),
        ),
        ui.column(
            4,
            ui.tooltip(
                ui.span(tooltip_icon, " Servo motor settings:"),
                "Select one or more servomotors and corresponding pads depending on your setup. \
                In most cases these applicable for bombers",
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
                choices=settings.DSHOT_OPTIONS,
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
                choices=settings.STACK_CHOICES,
                # width="95%",
            ),
        ),
        ui.column(
            4,
            ui.tooltip(
                ui.span(tooltip_icon, " Betaflight version:"),
                "Firmware version migh be not compatible with provided presets, e.g VD OSD settings. \
                I did my best to prevent tool from misconfiguration just raise Github issue if you find some errors",
                placement="right",
            ),
            ui.input_radio_buttons(
                id="betaflight_version",
                label="Betaflight version",
                choices=settings.BETAFLIGHT_VERSION_CHOICES,
                inline=True,
                # width="100%",
            ),
        ),
        ui.column(
            4,
            ui.tooltip(
                ui.span(tooltip_icon, " Stack settings:"),
                "'Blackbox' migh not work properly at some stacks and should be used only if you need that. \
                'Apply default settings' will apply switch and adjustment ranges.",
                placement="right",
            ),
            ui.input_checkbox_group(
                id="stack_settings",
                label="Stack settings:",
                choices={
                    "enable_blackbox": ui.span("Enable blackbox"),
                    "apply_defaults": ui.span("Apply default settings"),
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
                choices=settings.VTX_CHOICES,
                # width="95%",
            ),
        ),
        ui.column(
            4,
            ui.tooltip(
                ui.span(tooltip_icon, " VTX settings:"),
                "VTX power on switch will allow pilot to set power level during the fly. \
                PIT mode will keep the power on miminal value until drone Arm to prevent overheating. \
                Migh be unavailable on some transmitters",
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
                choices=settings.UART_CHOICES,
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
                    "apply_pids": ui.span("Apply PIDs"),
                    "apply_filters": ui.span("Apply Filters"),
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
