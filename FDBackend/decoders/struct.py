from pydantic import BaseModel

class Classification(BaseModel):
    ce: str = "未知"
    ch: str = "未知"
    rb: str = "未知"
    die: str = "未知"


class Decode_packet(BaseModel):
    partNumber: str
    vendor: str = "未知"
    type: str = "未知"
    density: str = "未知"
    deviceWidth: str = "未知"
    processNode: str = "未知"
    cellLevel: str = "未知"
    classification: Classification = Classification()
    voltage: str = "未知"
    generation: str = "未知"
    interface: dict = {}
    package: str = "未知"
    extraInfo: dict = {}
    flashId: list = []
    controller: list = []
    remark: str= "未知"
    url: list = []
    rawVendor: str = "未知"

class searchID_packet(BaseModel):
    partNumbers: list = []
    pageSize: str = "未知"
    pagesPerBlock: int = 0
    blocks: int = 0
    controllers: list = []