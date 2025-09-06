from dataclasses import dataclass, field
from enum import Enum, IntFlag
from typing import Dict, List, Union

from cereal import car
from panda.python import uds
from selfdrive.car import dbc_dict
from selfdrive.car.docs_definitions import CarFootnote, CarHarness, CarInfo, CarParts, Column
from selfdrive.car.fw_query_definitions import FwQueryConfig, Request, StdQueries, p16

Ecu = car.CarParams.Ecu


class CarControllerParams:
  def __init__(self, CP):
    self.STEER_STEP = 2                # how often we update the steer cmd
    self.STEER_DELTA_UP = 50           # torque increase per refresh, 0.8s to max
    self.STEER_DELTA_DOWN = 70         # torque decrease per refresh
    self.STEER_DRIVER_ALLOWANCE = 60   # allowed driver torque before start limiting
    self.STEER_DRIVER_MULTIPLIER = 50  # weight driver torque heavily
    self.STEER_DRIVER_FACTOR = 1       # from dbc
    self.ACC_MIN_DIST = 3              # stop and go min distance threshold
    self.ACC_MAX_DIST = 4.5            # stop and go max distance threshold

    if CP.carFingerprint in GLOBAL_GEN2:
      self.STEER_MAX = 1000
      self.STEER_DELTA_UP = 40
      self.STEER_DELTA_DOWN = 40
    elif CP.carFingerprint == CAR.IMPREZA_2020:
      self.STEER_MAX = 1439
    else:
      self.STEER_MAX = 2047


class SubaruFlags(IntFlag):
  SEND_INFOTAINMENT = 1


class CanBus:
  main = 0
  alt = 1
  camera = 2


class CAR:
  # Global platform
  ASCENT = "SUBARU ASCENT LIMITED 2019"
  IMPREZA = "SUBARU IMPREZA LIMITED 2019"
  IMPREZA_2020 = "SUBARU IMPREZA SPORT 2020"
  CROSSTREK_2020H = "SUBARU CROSSTREK LIMITED 2020 HYBRID"
  FORESTER = "SUBARU FORESTER 2019"
  FORESTER_2020H = "SUBARU FORESTER 2020 HYBRID"
  FORESTER_2022 = "SUBARU FORESTER 2022"
  OUTBACK = "SUBARU OUTBACK 6TH GEN"
  LEGACY = "SUBARU LEGACY 7TH GEN"

  # Pre-global
  FORESTER_PREGLOBAL = "SUBARU FORESTER 2017 - 2018"
  LEGACY_PREGLOBAL = "SUBARU LEGACY 2015 - 2017"
  LEGACY_PREGLOBAL_2018 = "SUBARU LEGACY 2018 - 2019"
  LEVORG_PREGLOBAL = "SUBARU LEVORG 2016"
  OUTBACK_PREGLOBAL = "SUBARU OUTBACK 2015 - 2017"
  OUTBACK_PREGLOBAL_2018 = "SUBARU OUTBACK 2018 - 2019"
  WRX_PREGLOBAL = "SUBARU WRX 2018"


class Footnote(Enum):
  GLOBAL = CarFootnote(
    "In the non-US market, openpilot requires the car to come equipped with EyeSight with Lane Keep Assistance.",
    Column.PACKAGE)


@dataclass
class SubaruCarInfo(CarInfo):
  package: str = "EyeSight Driver Assistance"
  car_parts: CarParts = field(default_factory=CarParts.common([CarHarness.subaru_a]))
  footnotes: List[Enum] = field(default_factory=lambda: [Footnote.GLOBAL])


CAR_INFO: Dict[str, Union[SubaruCarInfo, List[SubaruCarInfo]]] = {
  CAR.ASCENT: SubaruCarInfo("Subaru Ascent 2019-21", "All"),
  # Updated years to reflect your 2024
  CAR.OUTBACK: SubaruCarInfo("Subaru Outback 2020-24", "All", car_parts=CarParts.common([CarHarness.subaru_b])),
  CAR.LEGACY: SubaruCarInfo("Subaru Legacy 2020-22", "All", car_parts=CarParts.common([CarHarness.subaru_b])),
  CAR.IMPREZA: [
    SubaruCarInfo("Subaru Impreza 2017-19"),
    SubaruCarInfo("Subaru Crosstrek 2018-19", video_link="https://youtu.be/Agww7oE1k-s?t=26"),
    SubaruCarInfo("Subaru XV 2018-19", video_link="https://youtu.be/Agww7oE1k-s?t=26"),
  ],
  CAR.IMPREZA_2020: [
    SubaruCarInfo("Subaru Impreza 2020-22"),
    SubaruCarInfo("Subaru Crosstrek 2020-23"),
    SubaruCarInfo("Subaru XV 2020-21"),
  ],
  CAR.CROSSTREK_2020H: SubaruCarInfo("Subaru Crosstrek Hybrid 2020"),
  CAR.FORESTER: SubaruCarInfo("Subaru Forester 2019-21", "All"),
  CAR.FORESTER_2020H: SubaruCarInfo("Subaru Forester Hybrid 2020"),
  CAR.FORESTER_2022: SubaruCarInfo("Subaru Forester 2022-23", car_parts=CarParts.common([CarHarness.subaru_c])),
  CAR.FORESTER_PREGLOBAL: SubaruCarInfo("Subaru Forester 2017-18"),
  CAR.LEGACY_PREGLOBAL: SubaruCarInfo("Subaru Legacy 2015-17"),
  CAR.LEGACY_PREGLOBAL_2018: SubaruCarInfo("Subaru Legacy 2018-19"),
  CAR.LEVORG_PREGLOBAL: SubaruCarInfo("Subaru Levorg 2016"),
  CAR.OUTBACK_PREGLOBAL: SubaruCarInfo("Subaru Outback 2015-17"),
  CAR.OUTBACK_PREGLOBAL_2018: SubaruCarInfo("Subaru Outback 2018-19"),
  CAR.WRX_PREGLOBAL: SubaruCarInfo("Subaru WRX 2016-18"),
}

# --- Added: CAN-based fingerprints for selection (address -> dlc) ---
FINGERPRINTS: Dict[str, List[Dict[int, int]]] = {
  CAR.OUTBACK: [{
    0x002: 8, 0x040: 8, 0x041: 8, 0x044: 8, 0x048: 8, 0x049: 8, 0x04A: 8,
    0x110: 8, 0x111: 8, 0x112: 8, 0x118: 8, 0x119: 8, 0x11A: 8, 0x11E: 8,
    0x11F: 8, 0x121: 8, 0x122: 8, 0x124: 8, 0x138: 8, 0x139: 8, 0x13A: 8,
    0x13B: 8, 0x13C: 8, 0x145: 8, 0x146: 8, 0x151: 8, 0x153: 8, 0x155: 8,
    0x157: 8, 0x16A: 8, 0x174: 8, 0x220: 8, 0x221: 8, 0x222: 8, 0x228: 8,
    0x22A: 8, 0x22B: 8, 0x22C: 8, 0x22D: 8, 0x23B: 8, 0x240: 8, 0x241: 8,
    0x2D2: 8, 0x31E: 8, 0x31F: 8, 0x321: 8, 0x322: 8, 0x323: 8, 0x324: 8,
    0x325: 8, 0x326: 8, 0x327: 8, 0x328: 8, 0x32B: 8, 0x330: 8, 0x33A: 8,
    0x33B: 8, 0x342: 8, 0x345: 8, 0x346: 8, 0x347: 8, 0x34A: 8, 0x390: 8,
    0x393: 8, 0x3A2: 8, 0x3AC: 8, 0x3AD: 8, 0x3C4: 8, 0x3C5: 8, 0x3C6: 8,
    0x3C7: 8, 0x3D5: 8, 0x3FB: 8, 0x500: 8, 0x502: 8, 0x546: 8, 0x54F: 8,
    0x551: 8, 0x651: 8, 0x660: 8, 0x672: 8, 0x68D: 8, 0x6B1: 8, 0x6BB: 8,
    0x6BC: 8, 0x6CF: 8, 0x6DE: 8,
  }],
}

SUBARU_VERSION_REQUEST = bytes([uds.SERVICE_TYPE.READ_DATA_BY_IDENTIFIER]) + \
  p16(uds.DATA_IDENTIFIER_TYPE.APPLICATION_DATA_IDENTIFICATION)
SUBARU_VERSION_RESPONSE = bytes([uds.SERVICE_TYPE.READ_DATA_BY_IDENTIFIER + 0x40]) + \
  p16(uds.DATA_IDENTIFIER_TYPE.APPLICATION_DATA_IDENTIFICATION)

FW_QUERY_CONFIG = FwQueryConfig(
  requests=[
    Request(
      [StdQueries.TESTER_PRESENT_REQUEST, SUBARU_VERSION_REQUEST],
      [StdQueries.TESTER_PRESENT_RESPONSE, SUBARU_VERSION_RESPONSE],
    ),
  ],
)

FW_VERSIONS = {
  CAR.ASCENT: {
    (Ecu.abs, 0x7b0, None): [
      b'\xa5 \x19\x02\x00',
      b'\xa5 !\002\000',
      b'\xf1\x82\xa5 \x19\x02\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x85\xc0\xd0\x00',
      b'\005\xc0\xd0\000',
      b'\x95\xc0\xd0\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00d\xb9\x1f@ \x10',
      b'\000\000e~\037@ \'',
      b'\x00\x00e@\x1f@ $',
      b'\x00\x00d\xb9\x00\x00\x00\x00',
      b'\x00\x00e@\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xbb,\xa0t\a',
      b'\xbb,\xa0x\x07',
      b'\xf1\x82\xbb,\xa0t\x87',
      b'\xf1\x82\xbb,\xa0t\a',
      b'\xf1\x82\xd9,\xa0@\a',
      b'\xf1\x82\xd1,\xa0q\x07',
      b'\xd1,\xa0q\x07',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\x00\xfe\xf7\x00\x00',
      b'\x00>\xf0\x00\x00',
      b'\001\xfe\xf9\000\000',
      b'\x01\xfe\xf7\x00\x00',
      b'\x01\xfe\xfa\x00\x00',
    ],
  },
  CAR.LEGACY: {
    (Ecu.abs, 0x7b0, None): [
      b'\xa1\\  x04\x01',
      b'\xa1  \x03\x03',
      b'\xa1  \x02\x01',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x9b\xc0\x11\x00',
      b'\x9b\xc0\x11\x02',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00e\x80\x00\x1f@ \x19\x00',
      b'\x00\x00e\x9a\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xde\"a0\x07',
      b'\xe2"aq\x07',
      b'\xde,\xa0@\x07',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xa5\xf6\x05@\x00',
      b'\xa7\xf6\x04@\x00',
      b'\xa5\xfe\xc7@\x00',
    ],
  },
  CAR.IMPREZA: {
    (Ecu.abs, 0x7b0, None): [
      b'\x7a\x94\x3f\x90\x00',
      b'\xa2 \x185\x00',
      b'\xa2 \x193\x00',
      b'\xa2 \x194\x00',
      b'z\x94.\x90\x00',
      b'z\x94\b\x90\x01',
      b'\xa2 \x19`\x00',
      b'z\x94\f\x90\001',
      b'z\x9c\x19\x80\x01',
      b'z\x94\x08\x90\x00',
      b'z\x84\x19\x90\x00',
      b'\xf1\x00\xb2\x06\x04',
      b'z\x94\x0c\x90\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x7a\xc0\x0c\x00',
      b'z\xc0\x08\x00',
      b'\x8a\xc0\x00\x00',
      b'z\xc0\x04\x00',
      b'z\xc0\x00\x00',
      b'\x8a\xc0\x10\x00',
      b'z\xc0\n\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00\x64\xb5\x1f\x40\x20\x0e',
      b'\x00\x00d\xdc\x1f@ \x0e',
      b'\x00\x00e\x1c\x1f@ \x14',
      b'\x00\x00d)\x1f@ \a',
      b'\x00\x00e+\x1f@ \x14',
      b'\000\000e+\000\000\000\000',
      b'\000\000dd\037@ \016',
      b'\000\000e\002\037@ \024',
      b'\x00\x00d)\x00\x00\x00\x00',
      b'\x00\x00c\xf4\x00\x00\x00\x00',
      b'\x00\x00d\xdc\x00\x00\x00\x00',
      b'\x00\x00dd\x00\x00\x00\x00',
      b'\x00\x00c\xf4\x1f@ \x07',
      b'\x00\x00e\x1c\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xaa\x61\x66\x73\x07',
      b'\xbeacr\a',
      b'\xc5!`r\a',
      b'\xaa!ds\a',
      b'\xaa!`u\a',
      b'\xaa!dq\a',
      b'\xaa!dt\a',
      b'\xc5!ar\a',
      b'\xbe!as\a',
      b'\xc5!as\x07',
      b'\xc5!ds\a',
      b'\xc5!`s\a',
      b'\xaa!au\a',
      b'\xbe!at\a',
      b'\xaa\x00Bu\x07',
      b'\xc5!dr\x07',
      b'\xaa!aw\x07',
      b'\xaaaft\x07',
      b'\xaa!av\x07',
      b'\xaa\x01bt\x07',
      b'\xc5!ap\x07',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xe3\xe5\x46\x31\x00',
      b'\xe4\xe5\x061\x00',
      b'\xe5\xf5\x04\x00\x00',
      b'\xe3\xf5G\x00\x00',
      b'\xe3\xf5\a\x00\x00',
      b'\xe3\xf5C\x00\x00',
      b'\xf1\x00\xa4\x10@',
      b'\xe5\xf5B\x00\x00',
      b'\xe5\xf5$\000\000',
      b'\xe4\xf5\a\000\000',
      b'\xe3\xf5F\000\000',
      b'\xe4\xf5\002\000\000',
      b'\xe3\xd0\x081\x00',
      b'\xe3\xf5\x06\x00\x00',
      b'\xe3\xe5D1\x00',
      b'\xe3\xd5\x161\x00',
    ],
  },
  CAR.IMPREZA_2020: {
    (Ecu.abs, 0x7b0, None): [
      b'\xa2 \0314\000',
      b'\xa2 \0313\000',
      b'\xa2 !i\000',
      b'\xa2 !`\000',
      b'\xf1\x00\xb2\x06\x04',
      b'\xa2  `\x00',
      b'\xa2 !3\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x9a\xc0\x00\x00',
      b'\n\xc0\004\000',
      b'\x9a\xc0\x04\x00',
      b'\n\xc0\x04\x01',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\000\000eb\037@ \"',
      b'\x00\x00e\x8f\x1f@ )',
      b'\x00\x00eb\x00\x00\x00\x00',
      b'\x00\x00eq\x1f@ "',
      b'\x00\x00eq\x00\x00\x00\x00',
      b'\x00\x00e\x8f\x00\x00\x00\x00',
      b'\x00\x00e\xa4\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xca!ap\a',
      b'\xca!`p\a',
      b'\xca!`0\a',
      b'\xcc\"f0\a',
      b'\xcc!fp\a',
      b'\xca!a0\x07',
      b'\xca!f@\x07',
      b'\xca!fp\x07',
      b'\xf3"f@\x07',
      b'\xe6!`@\x07',
      b'\xe6!fp\x07',
      b'\xf3"fp\x07',
      b'\xe6"fp\x07',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xe6\xf5\004\000\000',
      b'\xe6\xf5$\000\000',
      b'\xe7\xf6B0\000',
      b'\xe7\xf5D0\000',
      b'\xf1\x00\xa4\x10@',
      b'\xf1\x00\xd7\x10@',
      b'\xe6\xf5D0\x00',
      b'\xe9\xf6F0\x00',
      b'\xe9\xf5\x02\x00\x00',
    ],
  },
  CAR.CROSSTREK_2020H: {
    # 2020 Crosstrek Hybrid - UDM / @revity
    # 2020 Crosstrek Hybrid - UDM / @Dave32
    # Ecu, addr, subaddr: ROM ID
    (Ecu.abs, 0x7b0, None): [
      b'\xa2 \x19e\x01',
      b'\xa2 !e\x01',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x9a\xc2\x01\x00',
      b'\n\xc2\x01\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00el\x1f@ #',
      b'\x00\x00el\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xd7!`@\x07',
      b'\xd7!`p\a',
      b'\xe9\xf5B0\x00',
      b'\xf4!`0\x07',
    ],
  },
  CAR.FORESTER: {
    (Ecu.abs, 0x7b0, None): [
      b'\xa3 \x18\x14\x00',
      b'\xa3  \024\000',
      b'\xa3 \031\024\000',
      b'\xa3  \x14\x01',
      b'\xf1\x00\xbb\r\x05',
      b'\xa3  $\x00',
      b'\xa3 \x18&\x00',
      b'\xa3 \x19&\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x8d\xc0\x04\x00',
      b'\x8d\xc0\x00\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00e!\x1f@ \x11',
      b'\x00\x00e\x97\x1f@ 0',
      b'\000\000e`\037@  ',
      b'\xf1\x00\xac\x02\x00',
      b'\x00\x00e!\x00\x00\x00\x00',
      b'\x00\x00e\x97\x00\x00\x00\x00',
      b'\x00\x00e^\x1f@ !',
      b'\x00\x00e^\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xb6"`A\x07',
      b'\xcf"`0\x07',
      b'\xcb\"`@\a',
      b'\xcb\"`p\a',
      b'\xf1\x00\xa2\x10\n',
      b'\xcf"`p\x07',
      b'\xcf\xa2`@\x07',
      b'\xb6\xa2`A\x07',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\032\xf6B0\000',
      b'\x1a\xf6F`\x00',
      b'\032\xf6b`\000',
      b'\x1a\xf6B`\x00',
      b'\x1a\xf6b0\x00',
      b'\x1a\xf6f`\x00',
      b'\x1a\xe6F1\x00',
      b'\x1a\xe6B1\x00',
    ],
  },
  CAR.FORESTER_2020H: {
    (Ecu.abs, 0x7b0, None): [
      b'\xa3 \x19T\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x8d\xc2\x00\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00eY\x1f@ !',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xd2\xa1`r\x07',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\x1b\xa7@a\x00',
    ],
  },
  CAR.FORESTER_2022: {
    (Ecu.abs, 0x7b0, None): [
      b'\xa3 !x\x00',
      b'\xa3 !v\x00',
      b'\xa3 "v\x00',
      b'\xa3 "x\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'-\xc0%0',
      b'-\xc0\x040',
      b'=\xc0%\x02',
      b'=\xc04\x02',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x04!\x01\x1eD\x07!\x00\x04,',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xd5"a0\x07',
      b'\xd5"`0\x07',
      b'\xf1"aq\x07',
      b'\xf1"`q\x07',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\x1d\x86B0\x00',
      b'\x1d\xf6B0\x00',
      b'\x1e\x86B0\x00',
      b'\x1e\xf6D0\x00',
      b'\x1a\xe6B1\x00',
      b'\x1a\xe6F1\x00',
    ],
  },
  CAR.FORESTER_PREGLOBAL: {
    (Ecu.abs, 0x7b0, None): [
      b'\x7d\x97\x14\x40',
      b'\xf1\x00\xbb\x0c\x04',
    ],
    (Ecu.eps, 0x746, None): [
      b'}\xc0\x10\x00',
      b'm\xc0\x10\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00\x64\x35\x1f\x40\x20\x09',
      b'\x00\x00c\xe9\x00\x00\x00\x00',
      b'\x00\x00c\xe9\x1f@ \x03',
      b'\x00\x00d\xd3\x1f@ \t',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xa7"@0\x07',
      b'\xa7"@q\x07',
      b'\xa7)\xa0q\a',
      b'\xba"@@\a',
      b'\xba"@p\a',
      b'\xba)\xa0@\x07',
      b'\xf1\x82\xa7)\xa0q\a',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\x1a\xf6F`\x00',
      b'\xda\xf2`\x80\x00',
      b'\xda\xf2`p\x00',
      b'\xda\xfd\xe0\x80\x00',
      b'\xdc\xf2@`\x00',
      b'\xdc\xf2\x60\x60\x00',
      b'\xdc\xf2`\x80\x00',
      b'\xdc\xf2`\x81\000',
      b'\xdc\xfd\xe0`\x00',
    ],
  },
  CAR.LEGACY_PREGLOBAL: {
    (Ecu.abs, 0x7b0, None): [
      b'k\x97D\x00',
      b'[\xba\xc4\x03',
      b'{\x97D\x00',
      b'[\x97D\000',
      b'[\x97D\x03',
      b'k\x9aD\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'[\xb0\x00\x01',
      b'K\xb0\x00\x01',
      b'k\xb0\x00\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00c\xb7\x1f@\x10\x16',
      b'\x00\x00c\x94\x1f@\x10\x08',
      b'\x00\x00c\x94\x00\x00\x00\x00',
      b'\x00\x00c\xec\x1f@ \x04',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xab*@r\a',
      b'\xa0+@p\x07',
      b'\xa0*@q\x07',
      b'\xb4"@0\x07',
      b'\xa0"@q\a',
      b'\xab+@p\x07',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xbe\xf2\x00p\x00',
      b'\xbf\xfb\xc0\x80\x00',
      b'\xbd\xf2\x00`\x00',
      b'\xbf\xf2\x00\x80\x00',
      b'\xbe\xfb\xc0p\x00',
    ],
  },
  CAR.LEGACY_PREGLOBAL_2018: {
    # 2018 Subaru Legacy 2.5i Premium - UDM / @kram322
    # 2018 Subaru Legacy - UDM / @Hassan
    # 2018 Subaru Legacy - UDM / @Brycey92
    # Ecu, addr, subaddr: ROM ID
    (Ecu.abs, 0x7b0, None): [
      b'\x8b\x97D\x00',
      b'\x8b\x9aD\x00',
      b'\x9b\x97D\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'{\xb0\x00\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00df\x1f@ \n',
      b'\x00\x00df\x00\x00\x00\x00',
      b'\x00\x00d\xfe\x1f@ \x15',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xb5\"@p\a',
      b'\xb5"@P\x07',
      b'\xb5+@q\x07',
      b'\xc4"@0\x07',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xbc\xf2\x00\x81\x00',
      b'\xf1\x00\xa4\x10@',
      b'\xbc\xf2\x00\x80\x00',
      b'\xbc\xfb\xc0`\x00',
      b'\xbb\xf2\x00`\x00',
    ],
  },
  CAR.LEVORG_PREGLOBAL: {
     # 2016 Subaru Levorg / @jpgnz
     # Ecu, addr, subaddr: ROM ID
     (Ecu.abs, 0x7b0, None): [
       b'j\x9c\x92\002',
       b'\x9a\x95\x92\x00',
     ],
     (Ecu.eps, 0x746, None): [
       b'Z\xb0\000\000',
       b'z\xb0\x00\x00',
     ],
     (Ecu.fwdCamera, 0x787, None): [
       b'\000\000c\xd3\000\000\000\000',
       b'\x00\x00eO\x1f@ %',
     ],
     (Ecu.engine, 0x7e0, None): [
       b'\xf1\x82\xa6\000\xa1t\a',
       b'\xcdi\xa00\x07',
     ],
     (Ecu.transmission, 0x7e1, None): [
       b'\xcb\xd9\000p\000',
       b'\xce\xed\xf0`\x00',
     ],
  },
  CAR.OUTBACK_PREGLOBAL: {
    (Ecu.abs, 0x7b0, None): [
      b'{\x9a\xac\x00',
      b'k\x97\xac\x00',
      b'\x5b\xf7\xbc\x03',
      b'[\xf7\xac\x03',
      b'{\x97\xac\x00',
      b'k\x9a\xac\x00',
      b'[\xba\xac\x03',
      b'[\xf7\xac\000',
      b'k\x97\xbc\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'k\xb0\x00\x00',
      b'[\xb0\x00\x00',
      b'\x4b\xb0\x00\x02',
      b'K\xb0\x00\x00',
      b'{\xb0\x00\x01',
      b'[\xb0\x00\x02',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00c\xec\x1f@ \x04',
      b'\x00\x00c\xd1\x1f@\x10\x17',
      b'\xf1\x00\xf0\xe0\x0e',
      b'\x00\x00c\x94\x00\x00\x00\x00',
      b'\x00\x00c\x94\x1f@\x10\b',
      b'\x00\x00c\xb7\x1f@\x10\x16',
      b'\000\000c\x90\037@\020\016',
      b'\x00\x00c\xec\x37@\x04',
      b'\x00\x00c\xd1\x1f@\x10\x16',
      b'\x00\x00c\xec\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xb4+@p\a',
      b'\xab\"@@\a',
      b'\xa0\x62\x41\x71\x07',
      b'\xa0*@q\a',
      b'\xab*@@\a',
      b'\xb4"@0\a',
      b'\xb4"@p\a',
      b'\xab"@s\a',
      b'\xab+@@\a',
      b'\xab+@p\x07',
      b'\xb4"@r\a',
      b'\xa0+@@\x07',
      b'\xa0\"@\x80\a',
      b'\xa0bAs\x07',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xbd\xfb\xe0\x80\x00',
      b'\xbe\xf2@\x80\x00',
      b'\xbf\xe2\x40\x80\x00',
      b'\xbf\xf2@\x80\x00',
      b'\xbe\xf2@p\x00',
      b'\xbd\xf2@`\x00',
      b'\xbd\xf2@\x81\000',
      b'\xbe\xfb\xe0p\000',
      b'\xbf\xfb\xe0b\x00',
      b'\xbe\xe2@`\x00',
      b'\xbd\xf2@\x80\x00',
    ],
  },
  CAR.OUTBACK_PREGLOBAL_2018: {
    (Ecu.abs, 0x7b0, None): [
      b'\x8b\x97\xac\x00',
      b'\x8b\x9a\xac\x00',
      b'\x9b\x97\xac\x00',
      b'\x8b\x97\xbc\x00',
      b'\x8b\x99\xac\x00',
      b'\x9b\x9a\xac\000',
      b'\x9b\x97\xbe\x10',
    ],
    (Ecu.eps, 0x746, None): [
      b'{\xb0\x00\x00',
      b'{\xb0\x00\x01',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00df\x1f@ \n',
      b'\x00\x00d\xfe\x1f@ \x15',
      b'\x00\x00d\x95\x00\x00\x00\x00',
      b'\x00\x00d\x95\x1f@ \x0f',
      b'\x00\x00d\xfe\x00\x00\x00\x00',
      b'\x00\x00e\x19\x1f@ \x15',
      b'\x00\x00df\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xb5"@p\a',
      b'\xb5+@@\a',
      b'\xb5"@P\a',
      b'\xc4"@0\a',
      b'\xb5b@1\x07',
      b'\xb5q\xe0@\a',
      b'\xc4+@0\a',
      b'\xc4b@p\a',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xbc\xf2@\x81\x00',
      b'\xbc\xfb\xe0\x80\x00',
      b'\xbc\xf2@\x80\x00',
      b'\xbb\xf2@`\x00',
      b'\xbc\xe2@\x80\x00',
      b'\xbc\xfb\xe0`\x00',
      b'\xbc\xaf\xe0`\x00',
      b'\xbb\xfb\xe0`\000',
      b'\xbc\xf2@`\x00',
    ],
  },
  CAR.WRX_PREGLOBAL: {
    # 2018 Subaru WRX / @cferra
    # 2016 Subaru WRX / @Hexinator
    # Ecu, addr, subaddr: ROM ID
    (Ecu.abs, 0x7b0, None): [
      b'\x8a\x95R\x01',
      b'j\x95R\x02',
    ],
    (Ecu.eps, 0x746, None): [
      b'z\xb0\x00\x00',
      b'Z\xb0\x00\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00d\xae\x1f@ \r',
      b'\x00\x00c\x93\x1f@\x10\r',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x82\xb2)\xa0P\x97',
      b'\xf1\x82\xa6)\xa0P\x07',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xcd\xfd\xd0\x80\x00',
      b'\xcb\xfd\xd0\x80\x00',
    ],
  },
  CAR.OUTBACK: {
    (Ecu.abs, 0x7b0, None): [
      b'\xa1  \x06\x01',
      b'\xa1  \a\x00',
      b'\xa1  \b\001',
      b'\xa1  \x06\x00',
      b'\xa1 "\t\x01',
      b'\xa1  \x08\x02',
      b'\xa1 \x06\x02',
      b'\xa1  \x07\x02',
      b'\xa1  \x08\x00',
      b'\xa1 "\t\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x9b\xc0\x10\x00',
      b'\x9b\xc0\x20\x00',
      b'\x1b\xc0\x10\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00eJ\x00\x1f@ \x19\x00',
      b'\000\000e\x80\000\037@ \031\000',
      b'\x00\x00e\x9a\x00\x00\x00\x00\x00\x00',
      b'\x00\x00e\x9a\x00\x1f@ 1\x00',
      b'\x00\x00eJ\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xbc,\xa0q\x07',
      b'\xbc\"`@\a',
      b'\xde"`0\a',
      b'\xf1\x82\xbc,\xa0q\a',
      b'\xf1\x82\xe3,\xa0@\x07',
      b'\xe2"`0\x07',
      b'\xe2"`p\x07',
      b'\xf1\x82\xe2,\xa0@\x07',
      b'\xbc"`q\x07',
      b'\xe3,\xa0@\x07',
      b'\xbc,\xa0u\x07',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xa5\xfe\xf7@\x00',
      b'\xa5\xf6D@\x00',
      b'\xa5\xfe\xf6@\x00',
      b'\xa7\x8e\xf40\x00',
      b'\xf1\x82\xa7\xf6D@\x00',
      b'\xa7\xf6D@\x00',
      b'\xa7\xfe\xf4@\x00',
      b'\xa5\xfe\xf8@\x00',
    ],
  },
}

DBC = {
  CAR.ASCENT: dbc_dict('subaru_global_2017_generated', None),
  CAR.IMPREZA: dbc_dict('subaru_global_2017_generated', None),
  CAR.IMPREZA_2020: dbc_dict('subaru_global_2017_generated', None),
  CAR.CROSSTREK_2020H: dbc_dict('subaru_global_2020_hybrid_generated', None),
  CAR.FORESTER: dbc_dict('subaru_global_2017_generated', None),
  CAR.FORESTER_2020H: dbc_dict('subaru_global_2017_generated', None),
  CAR.FORESTER_2022: dbc_dict('subaru_global_2022_generated', None),
  CAR.OUTBACK: dbc_dict('subaru_global_2017_generated', None),
  CAR.LEGACY: dbc_dict('subaru_global_2017_generated', None),
  CAR.FORESTER_PREGLOBAL: dbc_dict('subaru_forester_2017_generated', None),
  CAR.LEGACY_PREGLOBAL: dbc_dict('subaru_outback_2015_generated', None),
  CAR.LEGACY_PREGLOBAL_2018: dbc_dict('subaru_outback_2019_generated', None),
  CAR.LEVORG_PREGLOBAL: dbc_dict('subaru_forester_2017_generated', None),
  CAR.OUTBACK_PREGLOBAL: dbc_dict('subaru_outback_2015_generated', None),
  CAR.OUTBACK_PREGLOBAL_2018: dbc_dict('subaru_outback_2019_generated', None),
  CAR.WRX_PREGLOBAL: dbc_dict('subaru_forester_2017_generated', None),
}

GLOBAL_GEN2 = (CAR.OUTBACK, CAR.LEGACY)
PREGLOBAL_CARS = (CAR.FORESTER_PREGLOBAL, CAR.LEGACY_PREGLOBAL, CAR.LEGACY_PREGLOBAL_2018, CAR.LEVORG_PREGLOBAL, CAR.OUTBACK_PREGLOBAL, CAR.OUTBACK_PREGLOBAL_2018, CAR.WRX_PREGLOBAL)
GLOBAL_CARS_SNG = (CAR.ASCENT, CAR.IMPREZA, CAR.IMPREZA_2020, CAR.FORESTER, CAR.FORESTER_2020H, CAR.FORESTER_2022)
