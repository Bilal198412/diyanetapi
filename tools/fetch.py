#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib
import urllib2

def json_response(url, query_args):
    """docstring for fetch
    parameters : url, query_args
    """
    qdata = urllib.urlencode(query_args)
    request = urllib2.Request(url, qdata)
    response = urllib2.urlopen(request)
    if response.code == 200:
        return json.loads(response.read())
    else:
        return None


def dict_response(data):
    """docstring for filter"""
    mkeys = ['HicriTarih',
             'UlkeAdi', 'SehirAdi',
             'KibleAcisi', 'MoonSrc',
             'Imsak', 'Gunes', 'Ogle', 'Ikindi', 'Aksam', 'Yatsi']

    return dict(zip(mkeys, [data[k] for k in mkeys]))
