#!/usr/bin/env python3

import sys
import json
import pprint
from lib.dicts.urbandict import UrbanDict
from lib.dicts.mwdict import MWDict

def main():
    if len(sys.argv) < 2:
        raise TypeError("Input needed!")
    #dict = MWDict()
    dict = UrbanDict()
    res = dict.lookup(sys.argv[1])
    if type(res) is list:
        count = 1
        for item in res:
            print("""-----------------------------{0}--------------------------------""".format(count))
            count += 1
            dict_print(item, ["definition", "example"])

def dict_print(d, options):
    if d is None:
        return
    if options is None or len(options) == 0:
        p_print(dict)
        return
    for k, v in d.items():
        if k.lower() in options:
            print("""=================\n++ {0}\n=================""".format(k))
            print(v)

def p_print(s):
    pp = pprint.PrettyPrinter(indent=1)
    pp.pprint(s)

if __name__=="__main__":
    main()
