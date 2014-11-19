#!/usr/bin/env python
# -*- coding: utf-8 -*-

import apiv2
from apiv2 import prayerTimes

def main(*args, **kwargs):
    """docstring for main"""
    print prayerTimes(2,500,9149)
    
if __name__ == '__main__':
    print 'boo!...'
