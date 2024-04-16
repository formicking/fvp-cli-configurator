"""Defines UI options, constants and other settings"""

# --- Core component mappings ---
# Frame
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

# Motors
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

# Servos
SERVO_PAD_CHOICES = {
    "S9": "S9",
    "M8": "M8",
    "M7": "M7",
    "M6": "M6",
    "M5": "M5",
    "M4": "M4",
}

# Stack
STACK_CHOICES = {
    "sbf403": "SpeedyBee F403",
    "sbf404": "SpeedyBee F404",
    "gif403": "Galychyna",
    "vyriy": "Vyriy Drone + Q656 ESC",
    "dmf722": "Diatone mamba F722",
}

DSHOT_OPTIONS = {
    "none": "None",
    "d150": "D150",
    "d300": "D300",
    "d600": "D600",
}

# Betaflight configuration
BETAFLIGHT_CONFIGURATOR_CHOICES = {
    "43": {
        "OSD_CHOICES": {
            "vd": "Victory Drones",
            "none": "Default(No preset)",
        }
    },
    "44": {
        "OSD_CHOICES": {
            "io": "Victory Drones(Ovcharyk Edition)",
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

UART_CHOICES = {"2": "UART 2", "6": "UART 6"}


# VTX
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

# --- Configuration path ---
VTX_PATH_MAPPING = {
    "fre72": "presets/vtx/foxeer/reaper_extreme_v2.txt",
    "fre40": "presets/vtx/foxeer/reaper_extreme_v1.txt",
    "fri40": "presets/vtx/foxeer/reaper_infinity.txt",
    "rms48": "presets/vtx/rushfpv/max_solo.txt",
    "rts48": "presets/vtx/rushfpv/tank_solo.txt",
    "lts48": "presets/vtx/readytosky/lts.txt",
    "afd40": "presets/vtx/akk/fx2_dominator.txt",
    "aul40": "presets/vtx/akk/ultra_long_range.txt",
    "gmp72": "presets/vtx/geprc/maten_pro_v2.txt",
    "gmp40": "presets/vtx/geprc/maten_pro_v1.txt",
    "blw40": "presets/vtx/blitz/whoop.txt",
}
