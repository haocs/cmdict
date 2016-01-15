#!/usr/bin/env python3
import json, requests
from lib.dicts.dictbase import DictBase

class MWDict(DictBase):

    def __init__(self):
        self.api = "http://www.dictionaryapi.com/api/v1/references/collegiate/xml/"
        self.key =  "c7a96b80-0e33-4abe-986e-a45f7d91aad1"

    def formatter(lookup):
        def format(*args):
            formatted_res = []
            raw_res = lookup(*args)
            formatted_res = raw_res
            return formatted_res
        return format

    @formatter
    def lookup(self, word):
        url = self.api + word + "?key=" + self.key
        res = requests.get(url)
        result = {}
        if res.status_code == 200:
            result = res.text
        return result

