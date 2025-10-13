from migen.build.generic_platform import *


_io = [
    # Clk / Rst.
    ("clk27",  0, Pins("H11"), IOStandard("LVCMOS33")),

    # Serial.
    ("serial", 0,
        Subsignal("rx", Pins("T13")), # CARD1:1
        Subsignal("tx", Pins("M11")), # CARD1:11
        IOStandard("LVCMOS33")
    ),

    # HDMI.
    ("hdmi", 0,
        Subsignal("clk_p",   Pins("CARD1:68")),
        Subsignal("clk_n",   Pins("CARD1:70")),
        Subsignal("data0_p", Pins("CARD1:64")),
        Subsignal("data0_n", Pins("CARD1:62")),
        Subsignal("data1_p", Pins("CARD1:58")),
        Subsignal("data1_n", Pins("CARD1:56")),
        Subsignal("data2_p", Pins("CARD1:52")),
        Subsignal("data2_n", Pins("CARD1:50")),
        Subsignal("hdp", Pins("CARD1:154"), IOStandard("LVCMOS33")),
        Subsignal("cec", Pins("CARD1:152"), IOStandard("LVCMOS33")),
        #Subsignal("sda", Pins("CARD1:95")), # Conflict with eth mdc
        #Subsignal("scl", Pins("CARD1:97")), # Conflict with eth mdio
        Misc("PULL_MODE=NONE"),
    ),

    # Leds
    ("led1", 0,  Pins( "CARD1:44"), IOStandard("LVCMOS33")),
    ("led2", 1,  Pins( "CARD1:46"), IOStandard("LVCMOS33")),
    ("led3", 3,  Pins( "CARD1:40"), IOStandard("LVCMOS33")),
    ("led4", 2,  Pins( "CARD1:42"), IOStandard("LVCMOS33")),
    ("led5", 4,  Pins( "CARD1:98"), IOStandard("LVCMOS33")),
    ("led6", 5,  Pins("CARD1:136"), IOStandard("LVCMOS33")),

    # RGB Led.
    ("rgb_led", 0, Pins("CARD1:45"), IOStandard("LVCMOS33")),

    # Buttons.
    ("btn_1", 0,  Pins( "CARD1:15"), IOStandard("LVCMOS33")),
    ("btn_2", 1,  Pins("CARD1:165"), IOStandard("LVCMOS15")),
    ("btn_3", 2,  Pins("CARD1:163"), IOStandard("LVCMOS15")),
    ("btn_4", 3,  Pins("CARD1:159"), IOStandard("LVCMOS15")),
    ("btn_5", 4,  Pins("CARD1:157"), IOStandard("LVCMOS15")),

]

_connectors = [
    ["CARD1",
        # A.
        # -------------------------------------------------
        "---", # 0
        #     GND GND  5V  5V  5V  5V GND GND  NC   ( 1-10).
        " T13 --- --- --- --- --- --- --- --- ---",
        #      NC GND GND      NC  NC  NC GND GND   (11-20).
        " M11 --- --- --- T10 --- --- --- --- ---",
        #  NC 3V3  NC 3V3 GND GND                   (21-30).
        " --- --- --- --- --- ---  T6 R16  P6 P15",
        # GND GND                 GND GND           (31-40).
        " --- ---  T7 P16  R8 N15 --- ---  T8  N16",
        #         GND                 GND GND       (41-50).
        "  M6 N14 --- L16  T9 L14  P9 --- --- K15",
        #             GND GND                 GND   (51-60).
        " P11 K14 T11 --- --- K16 R11 J15 T12 ---",
        # GND                 GND                   (61-70).
        " --- H16 R12 H14 P13 --- R13 G16 T14 H15",
        # GND GND                                   (71-72).
        " --- ---",
        # B.
        # -------------------------------------------------
        #                                      NC   (73-82).
        " M15 L13 M14 K11 F13 K12 G12 K13 T15 ---",
        #                  NC  NC                   (83-92).
        " J16 H13 J14 J12 --- --- G14 H12 G15 G11",
        #  NC  NC                  NC  NC      NC  (93-102).
        " --- --- F14 B10 F16 A13 --- --- E15 ---",
        #      NC  NC  NC      NC      NC  NC  NC  (103-112).
        " D15 --- --- --- A15 --- B14 --- --- ---",
        #      NC      NC  NC  NC      NC      NC  (113-122).
        " A14 --- B13 --- --- --- C12 --- B12 ---",
        #      NC      NC GND GND                  (123-132).
        " A12 --- C11 --- --- --- B11 E16 A11 F15",
        # GND GND          NC GND GND      NC      (133-142).
        " --- --- C10 C13 --- --- --- D16 --- E14",
        #     GND GND                 GND GND      (143-152).
        "  B8 --- ---  C9  C6  A9  A7 --- --- L12",
        #         GND GBD                 GND GND  (153-162).
        "  A6 J11 --- ---  C7  E9  D7  E8 --- ---",
        #     VCC     VCC GND GND     VCC     GND  (163-172).
        "  T2 ---  T3 --- --- ---  T4 ---  T5 ---",
        # GND VCC             GND GND              (173-182).
        " --- ---  N6 F10  N7 --- --- D11  N9 D10",
        #     GND GND      NC  NC GND GND          (183-192).
        "  R9 --- --- E10 --- --- --- ---  N8 R7",
        #         GND GND  NC      NC      NC  NC  (193-202).
        "  L9  P7 --- --- ---  M6 ---  L8 --- ---",
        #  NC  NC                                  (203-204).
        " --- ---",
    ],
]

class Platform(GenericPlatform):
    default_clk_name = "clk27"
    default_clk_period = 1e9/27e6

    def __init__(self):
        GenericPlatform.__init__(self, io=_io, connectors=_connectors, device="not_a_real_device")