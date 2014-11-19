#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from pprint import pprint

def data2json(data, file, folder='_json/', ext='.json'):
    fullPath = folder + file + ext
    f = open(fullPath, 'w')
    f.write('%s' % json.dumps(data))
    f.close()
    print '%s \t OK' % fullPath
    pass

def filterize(data):
    f = {}
    for i in data:
        f[i['Text']] = dict( Text = i['Text'],
                Value = i['Value'])
    return f
