#!/usr/bin/env python3

import sys, pprint
from lib.dicts.urbandict import UrbanDict
from lib.dicts.mwdict import MWDict

def main():
    if len(sys.argv) < 2:
        raise TypeError("Input needed!")
    dict = MWDict()
    res = dict.lookup(sys.argv[1])
    p_print(res)

def p_print(s):
    pp = pprint.PrettyPrinter(indent=3)
    pp.pprint(s)

if __name__=="__main__":
    main()
