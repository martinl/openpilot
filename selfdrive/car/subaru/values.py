# flake8: noqa

from selfdrive.car import dbc_dict
from cereal import car
Ecu = car.CarParams.Ecu

class CAR:
  IMPREZA = "SUBARU IMPREZA LIMITED 2019"
  OUTBACK = "SUBARU OUTBACK 2015 - 2018"
  LEGACY = "SUBARU LEGACY 2015 - 2018"
  FORESTER = "SUBARU FORESTER 2017"
  ASCENT = "SUBARU ASCENT 2020"

FINGERPRINTS = {
  CAR.IMPREZA: [
  # SUBARU IMPREZA LIMITED 2019 (commaai)
  {
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 280: 8, 281: 8, 290: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 544: 8, 545: 8, 546: 8, 552: 8, 554: 8, 557: 8, 576: 8, 577: 8, 722: 8, 801: 8, 802: 8, 805: 8, 808: 8, 816: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1650: 8, 1657: 8, 1658: 8, 1677: 8, 1697: 8, 1722: 8, 1743: 8, 1759: 8, 1786: 5, 1787: 5, 1788: 8, 1809: 8, 1813: 8, 1817: 8, 1821: 8, 1840: 8, 1848: 8, 1924: 8, 1932: 8, 1952: 8, 1960: 8
  },
  # SUBARU XV ACTIVE 2.0 2018 (mlp)
  {
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 256: 8, 280: 8, 281: 8, 290: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 372: 8, 544: 8, 545: 8, 546: 8, 554: 8, 557: 8, 576: 8, 577: 8, 722: 8, 801: 8, 802: 8, 805: 8, 808: 8, 811: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1650: 8, 1657: 8, 1658: 8, 1677: 8, 1697: 8, 1759: 8, 1786: 5, 1787: 5, 1788: 8
  },
  # SUBARU XV 2.0i-S 2018 (aztan)
  {
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 280: 8, 281: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 372: 8, 552: 8, 557: 8, 576: 8, 577: 8, 722: 8, 808: 8, 811: 8, 816: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1640: 8, 1650: 8, 1657: 8, 1658: 8, 1677: 8, 1722: 8, 1759: 8, 1786: 5, 1787: 5, 1788: 8
  },
  # END IMPREZA
  ],
  CAR.OUTBACK: [
  # OUTBACK PREMIUM 2.5i 2015 (Bugsy)
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 346: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 640: 8, 642: 8, 644: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 977: 8, 1632: 8, 1745: 8, 1786: 5, 1882: 8, 2015: 8, 2016: 8, 2024: 8
  },
  # OUTBACK PREMIUM 2.5i 2015 (Mark77)
  #{
  #  2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 604: 8, 640: 8, 642: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 977: 8, 1632: 8, 1745: 8, 1786: 5
  #},
  # OUTBACK LIMITED 2.5i 2016 (mokahat)
  #{
  #  2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 604: 8, 640: 8, 642: 8, 644: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 885: 8, 977: 8, 1788: 8
  #},
  # OUTBACK PREMIUM 3.6i 2015 (aidrive)
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 392: 8, 604: 8, 640: 8, 642: 8, 644: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 977: 8, 1632: 8, 1745: 8, 1779: 8, 1786: 5
  },
  # OUTBACK LIMITED 2017 (spacebtc281)
  #{
  #  2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 604: 8, 640: 8, 642: 8, 644: 8, 805: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1632: 8, 1640: 8, 1736: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8, 1792: 8, 1793: 4, 1872: 8, 1882: 8, 1937: 8, 1953: 8, 1968: 8, 1976: 8, 2015: 8, 2016: 8, 2024: 8
  #},
  # OUTBACK LIMITED 2.5i 2018 (aderbique)
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 316: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 554: 8, 604: 8, 640: 8, 642: 8, 644: 8, 805: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1614: 8, 1632: 8, 1657: 8, 1658: 8, 1672: 8, 1722: 8, 1736: 8, 1743: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8
  }
  # OUTBACK 2018 (naboo)
  #{
  #  2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 316: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 392: 8, 604: 8, 640: 8, 642: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1614: 8, 1632: 8, 1640: 8, 1657: 8, 1658: 8, 1672: 8, 1743: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8
  #},
  # END OUTBACK
  ],
  CAR.FORESTER: [
  # FORESTER PREMIUM 2.5i 2017
  {
    2: 8, 112: 8, 117: 8, 128: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 340: 7, 342: 8, 352: 8, 353: 8, 354: 8, 355: 8, 356: 8, 554: 8,604: 8, 640: 8, 641: 8, 642: 8, 805: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 886: 1, 888: 8, 977: 8, 1398: 8, 1632: 8, 1743: 8, 1744: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8, 1882: 8, 1895: 8, 1903: 8, 1986: 8, 1994: 8, 2015: 8, 2016: 8, 2024: 8
  },
  # Subaru Forester 2.5L CVT Touring w/EyeSight (Oreo)
  #{
  #  2: 8, 112: 8, 117: 8, 128: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 340: 7, 342: 8, 352: 8, 353: 8, 354: 8, 355: 8, 356: 8, 554: 8, 604: 8, 640: 8, 641: 8, 642: 8, 644: 8, 805: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 886: 1, 888: 8, 890: 8, 977: 8, 1398: 8, 1632: 8, 1736: 8, 1743: 8, 1744: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8, 1895: 8, 1903: 8, 1986: 8, 1994: 8
  #}
  # END FORESTER
  ],
  CAR.LEGACY: [
  # LEGACY LIMITED 2.5i 2015 (temp disable, inconsistent with Mark77 Outback)
  #{
  #  2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 604: 8, 640: 8, 642: 8, 644: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 977: 8, 1632: 8, 1745: 8, 1786: 5
  #},
  # LEGACY 2.5i 2017
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 392: 8, 604: 8, 640: 8, 642: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1632: 8, 1640: 8, 1736: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8
  },
  # LEGACY 2018 (Hassan)
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 316: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 392: 8, 604: 8, 640: 8, 642: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1614: 8, 1632: 8, 1640: 8, 1657: 8, 1658: 8, 1672: 8, 1722: 8, 1743: 8, 1745: 8, 1778: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8, 2015: 8, 2016: 8, 2024: 8
  },
  # END LEGACY
  ],
}

# Use only FPv2
IGNORED_FINGERPRINTS = [CAR.IMPREZA]

FW_VERSIONS = {
  CAR.IMPREZA: {
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [b'\x7a\x94\x3f\x90\x00'],
    (Ecu.eps, 0x746, None): [b'\x7a\xc0\x0c\x00'],
    (Ecu.srs, 0x780, None): [b'\x00\x92\x15\x16\x00'],
    (Ecu.fwdCamera, 0x787, None): [b'\x00\x00\x64\xb5\x1f\x40\x20\x0e'],
    (Ecu.engine, 0x7e0, None): [b'\xaa\x61\x66\x73\x07'],
    (Ecu.transmission, 0x7e1, None): [b'\xe3\xe5\x46\x31\x00'],
  },
  CAR.FORESTER: {
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [b'}\x97\x14@'],
    (Ecu.eps, 0x746, None): [b'}\xc0\x10\x00'],
    (Ecu.srs, 0x780, None): [b'\x90\x00%\x00'],
    (Ecu.fwdCamera, 0x787, None): [b'\x00\x00d5\x1f@ \t'],
    (Ecu.engine, 0x7e0, None): [b'\xba"@p\x07'],
    #(Ecu.transmission, 0x7e1, None): [b'\xe3\xe5\x46\x31\x00'],
  },
}


STEER_THRESHOLD = {
  CAR.IMPREZA: 80,
  CAR.OUTBACK: 600,
  CAR.LEGACY: 600,
  CAR.FORESTER: 600,
}

ECU_FINGERPRINT = {
  Ecu.fwdCamera: [290, 356],   # steer torque cmd
}

DBC = {
  CAR.IMPREZA: dbc_dict('subaru_global_2017', None),
  CAR.ASCENT: dbc_dict('subaru_global_2017', None),
  CAR.OUTBACK: dbc_dict('subaru_outback_2015_eyesight', None),
  CAR.LEGACY: dbc_dict('subaru_outback_2015_eyesight', None),
  CAR.FORESTER: dbc_dict('subaru_forester_2017', None),
}
