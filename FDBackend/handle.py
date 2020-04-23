# -*- coding: utf-8 -*-
# generate by new_app on 2020/04/23 11:35

import time
import json

from FDBackend.decoders.kioxia import Decoder
from core.web import WebHandler, JsonResponse, FileResponse
from FDBackend.decoders.struct import searchID_packet

db = json.load(
    open("FDBackend/fdb.json", "r")
)

class Index(WebHandler):
    async def get(self):
        return JsonResponse({"result": True, "time": int(time.time()), "server": "NullcatServer/FDBackend"})

class test(WebHandler):
    async def get(self):
        return FileResponse("FDBackend/fdb.json", content_type="application/json")

class decoder(WebHandler):
    async def get(self):
        pn = self.request.GET.get("pn")
        if pn:
            decode = Decoder(pn)
            return JsonResponse({"result": True, "data": decode.dict()})
        else:
            return JsonResponse({"result": False, "message": "Missing argument 'pn'"})

class searchId(WebHandler):
    async def get(self):
        lid = self.request.GET.get("id")
        if lid:
            if lid in db["iddb"]:
                c = db["iddb"][lid]
                pkg = searchID_packet(
                    partNumbers=c["n"],
                    controllers=c.get("t", []),
                    pageSize=str(c["s"])+"K",
                    pagesPerBlock=c["p"],
                    blocks=c["b"]
                )
                return JsonResponse({"result": True, "data": {lid: pkg.dict()}})
            else:
                return JsonResponse({"result": True, "data": []})
        else:
            return JsonResponse({"result": False, "message": "Missing argument 'id'"})