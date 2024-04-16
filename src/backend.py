"""Backend module with all additional functions needed to support configurator app."""

from pathlib import Path
import settings


def read_file(filename):
    """Function for reading configuration files"""
    with open(filename, encoding="utf-8") as config:
        return config.read()


def parse_input(user_input):
    """Function for parsing user input from UI
    user_input contains user settings selected on frontend"""

    osd = settings.BETAFLIGHT_CONFIGURATOR_CHOICES[user_input.betaflight_version()][
        "OSD_CHOICES"
    ]
    components = f"Drone specification:\n \
    Frame: {settings.FRAME_CHOICES[user_input.frame_size()][user_input.frame()]} ({settings.FRAME_SIZE_CHOICES[user_input.frame_size()]})\n \
    Motors: {settings.MOTOR_CHOICES[user_input.frame_size()][user_input.motor()]}\n \
    Stack: {settings.STACK_CHOICES[user_input.stack()]}\n \
    VTX: {settings.VTX_CHOICES[user_input.vtx()]}\n\n"
    other_settings = f"Settings:\n \
    Stack settings: {user_input.stack_settings()}\n \
    VTX settings: {user_input.vtx_settings()}\n \
    Advanced settings: {user_input.additional_settings()}\n \
    Betaflight version: {settings.BETAFLIGHT_VERSION_CHOICES[user_input.betaflight_version()]}\n \
    DSHOT configuration: {user_input.dshot()}\n \
    RX UART: {user_input.rx_uart()}\n \
    OSD Style: {osd[user_input.osd_options()]}\n\n"

    results = components + other_settings

    if "drop_servo" in user_input.servo_settings():
        results += f"Drop servo motor on pad {user_input.drop_servo_pad()}\n"

    if "camera_servo" in user_input.servo_settings():
        results += f"Camera servo motor on pad {user_input.camera_servo_pad()}\n"

    print(results)
    return results


def set_vtx_power(user_input):
    """Function for parsing selected VTX table to retreive power levels for specific model
    And generating dynamic configuration"""
    if "set_vtx_power" in user_input.vtx_settings():
        filepath = (
            Path(__file__).parent
            / "betaflight"
            / settings.VTX_PATH_MAPPING[user_input.vtx()]
        )
        vtx_config = read_file(filepath).split("\n")
        max_level = [s for s in vtx_config if "vtxtable powerlevels" in s][0].split()[
            -1
        ]
        return f"# vtx power level on switch\nvtx 0 2 0 0 1 900 1100\nvtx 1 2 0 0 3 1400 1600\nvtx 3 2 0 0 {max_level} 2000 2100\n\n"

    return "\n"


def set_pit_mode(user_input):
    """Function for setting VTX to PIT mod to prevent overheating during tests"""
    if "enable_pit_mode" in user_input.vtx_settings():
        return "# enable PIT mode\nset vtx_low_power_disarm = UNTIL_FIRST_ARM\n\n"
    return "\n"
