#!/usr/bin/env python3

import json, requests
from lib.dicts.dictbase import DictBase

class UrbanDict(DictBase):
    """ Lookup on urban dick~tionary :) """
    def __init__(self):
        _API = "http://api.urbandictionary.com/v0/define?term="
        self.api = _API

    def formatter(lookup):
        def format(*args):
            formatted_res = [] 
            raw_res = lookup(*args)
            if "list" in raw_res:
                items = raw_res["list"]
                for item in items:
                    formatted_res.append([{"Word":item['word'].rstrip()}, {"Definition":item['definition'].rstrip()}, {"Example":item['example'].rstrip()}])
                    #formatted_res.append(item)
            return formatted_res

        return format

    @formatter
    def lookup(self, word):
        url = self.api + word
        res = requests.get(url)
        result = {}
        if res.status_code == 200:
            result = json.loads(res.text)
        return result

