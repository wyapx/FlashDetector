# -*- coding: utf-8 -*-
# generate by new_app on 2020/04/23 11:35

from core.route import path
from . import handle

pattern = [
    path("^/$", handle.Index),
    path("^/decode$", handle.decoder),
    path("^/searchId$", handle.searchId),
    path("^/test$", handle.test)
]
