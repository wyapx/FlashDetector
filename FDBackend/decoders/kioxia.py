from .struct import Decode_packet
from .trans import translate

vol_define = {
    "V": "3.3V",
    "Y": "1.8V",
    "A": "Vcc: 3.3V, VccQ: 1.8V",
    "B": "Vcc: 3.3V, VccQ: 1.65V-3.6V",
    "D": "Vcc: 3.3V/1.8V, VccQ: 3.3V/1.8V",
    "E": "Vcc: 3.3V, VccQ: 3.3V/1.8V",
    "F": "Vcc: 3.3V, VccQ: 3.3V/1.8V (UNOFFICIAL)",
    "J": "Vcc: 3.3V, VccQ: 1.8V/1.2V (UNOFFICIAL)"
}

density_define = {
    "M8": "256",
    "M9": "512",
    "G0": "1Gbit",
    "G1": "2Gbit",
    "G2": "4Gbit",
    "G3": "8Gbit",
    "G4": "16Gbit",
    "GA": "24Gbit",
    "G5": "32Gbit",
    "GB": "48Gbit",
    "G6": "64Gbit",
    "GC": "96Gbit",
    "G7": "128Gbit",
    "GD": "192Gbit",
    "G8": "256Gbit",
    "GE": "384Gbit",
    "G9": "512Gbit",
    "GF": "768Gbit",
    "T0": "1TBit",
    "T1": "2TBit",
    "T2": "4TBit",
    "T3": "8TBit",
    "TG": "1.5TBit"
}

level_define = {
    "S": "SLC",
    "H": "eSLC",  # eSLC
    "D": "MLC",
    "E": "eMLC",  # eMLC
    "J": "MLC",
    "C": "MLC",
    "T": "TLC",
    "U": "eTLC",  # eTLC
    "V": "TLC",
    "X": "TLC",
    "W": "TLC",
    "F": "QLC",  # QLC
}

processNode_define = {
    "A": "130 nm",
    "B": "90 nm",
    "C": "70 nm",
    "D": "56 nm",
    "E": "43 nm",
    "F": "32 nm",
    "G": "24 nm A-type",
    "H": "24 nm B-type",
    "J": "19 nm",
    "K": "A19 nm",
    "L": "15 nm",
    "2": "BiCS2",
    "3": "BiCS3",
    "4": "BiCS4"
}

size_define = {
    "0": ["4KB", "256KB"],
    "1": ["4KB", "512KB"],
    "2": [">4KB", ">512KB"],
    "3": ["2KB", "128KB"],
    "4": ["2KB", "256KB"],
    "5": ["4KB", "256KB"],
    "6": ["4KB", "512KB"],
    "7": [">4KB", ">512KB"],
    "8": ["2KB", "128KB"],
    "9": ["2KB", "256KB"],
    "A": ["8KB", "2MB"],
    "B": ["16KB", "8MB"],
    "C": ["16KB 1pl", "4MB"],
    "D": ["16KB 2pl", "4MB"],
    "F": ["16KB 4pl", "4MB"]
}

classification_define = {
    "0": [1, 1],  # Ch, nCE
    "I": [1, 1],
    "2": [1, 2],
    "K": [1, 2],
    "4": [2, 2],
    "M": [2, 2],
    "7": [1, 4],
    "R": [1, 4],
    "8": [-2, 4],
    "S": [-2, 4],
    "A": [-2, 6],
    "U": [-2, 6],
    "B": [-2, 8],
    "V": [-2, 8],
    "D": [4, 4],
    "E": [4, 8]
}

bga_packet_define = {
    "1": "BGA224 (14 x 18 x 1.46)",
    "2": "BGA224 (14 x 18 x 1.46)",
    "3": "BGA60 (8.5 x 13)",
    "4": "BGA60 (9 x 11)",
    "5": "BGA60 (10 x 13)",
    "6": "BGA60 (8.5 x 13)",
    "7": "BGA60 (9 x 11)",
    "8": "BGA60 (10 x 13)",
    "9": "BGA132 (12 x 18 x 1.4)",
    "A": "BGA132 (12 x 18 x 1.85)",
    "B": "BGA224 (14 x 18 x 1.35)",
    "C": "BGA132",
    "D": "BGA132",
    "E": "BGA272",
    "F": "BGA272",
    "G": "BGA272",
    "H": "BGA132",
    "J": "BGA152",
    "K": "BGA152",
    "N": "BGA152",
    "P": "BGA132"
}

nand_define = ("N", "D", "T", "L")
ent_define = ("H", "E", "U", "V")
x8_define = ("0", "1", "2", "3", "4", "A", "B", "C", "D", "F")
x16_define = ("5", "6", "7", "8", "9")
BGA_define = ("BA", "BB")


def Decoder(pn: str):
    dp = Decode_packet(partNumber=pn)
    if pn[0] != "T":
        return False
    try:
        dp.vendor = translate("kioxia")
        dp.rawVendor = "kioxia"
        dp.extraInfo[translate("noPb")] = "是"
        dp.extraInfo[translate("noHalogen")] = "否"
        if pn[1] == "H":
            dp.extraInfo[translate("multiChip")] = "是"
        else:
            dp.extraInfo[translate("multiChip")] = "否"
        if pn[4] in nand_define:
            dp.type = translate("nand")
        else:
            dp.type = "Unknown"
        dp.voltage = vol_define.get(pn[5])
        dp.density = density_define.get(pn[6:8])
        if pn[8] in ent_define:
            dp.extraInfo[translate("enterprise")] = "是"
        else:
            dp.extraInfo[translate("enterprise")] = "否"
        dp.cellLevel = level_define.get(pn[9])
        # width = pn[10]
        if pn[9] in x8_define:
            dp.deviceWidth = "x8"
        elif pn[9] in x16_define:
            dp.deviceWidth = "x16"
        size = size_define.get(pn[9], [0, 0])
        dp.extraInfo[translate("pageSize")] = size[0]
        dp.extraInfo[translate("blockSize")] = size[1]
        dp.processNode = processNode_define.get(pn[10])
        classified = classification_define.get(pn[13])
        dp.classification.ch = classified[0]
        dp.classification.ce = classified[1]
        if pn[11:13] in BGA_define:
            dp.package = bga_packet_define.get(pn[14])
    except IndexError:
        pass
    return dp
