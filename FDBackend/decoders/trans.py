name = {
    "kioxia":     "铠侠",
    "nand":       "NAND",
    "multiChip":  "多晶片",
    "enterprise": "企业级",
    "pageSize":   "页大小",
    "blockSize":  "块大小",
    "noPb":       "无铅",
    "noHalogen":  "无卤"
}

def translate(string):
    if string in name:
        return name[string]
    return string