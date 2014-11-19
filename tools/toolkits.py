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

def fireBaseIO(app, url, data, method = 'patch',
            bigdata = False, *args, **kwargs):
    """docstring for fireBaseIO"""
    exactUrl = 'https://%s.firebaseio.com/%s.json' % (app,url)
    if bigdata:
        for k,v in data.iteritems():
            exactUrl = 'https://%s.firebaseio.com/%s/%s.json' % ( app, url, k)
            requests.patch (exactUrl, json.dumps ( v ))
            print ( 'Data sent to %s' %exactUrl)
        return
    if method == 'patch':
        requests.patch(exactUrl, json.dumps(data))
    elif method == 'put':
        requests.put(exactUrl, json.dumps(data))
    elif method == 'post':
        requests.post(exactUrl, json.dumps(data))
    print 'Data sent to %s with %s method' %(exactUrl, method)
    return
