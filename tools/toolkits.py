#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


def json_dumps(data):
    """ Takes dictionary data and dumps and encodes/escapes in unicode """
    return json.dumps(data,  ensure_ascii=False).encode('utf8')


def data2json(data, file, folder='_json/', ext='.json'):
    """
        Dumps the json data as a new file
    """
    fullPath = folder + file + ext
    f = open(fullPath, 'w')
    f.write('%s' % json.dumps(data))
    f.close()
    print '%s \t OK' % fullPath
    pass


def filterize(data):
    """
        Generates a new dictionary and strips Text and Value keys.
        New dictionary format is : data[Value] = Text
    """
    f = {}
    for i in data:
        f[i['Text']] = dict(Text=i['Text'],
                            Value=i['Value'])
    return f
