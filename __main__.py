#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import *
from pprint import pprint

def main(*args, **kwargs):
    """docstring for main"""
    pprint ( prayerTimes(stateName = 9149,
                      countryName = 2,
                      name = 9149) )

if __name__ == '__main__':
    main()
