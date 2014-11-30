#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import logging


def fireBaseIO(app, path, data=None, method='get',
               bigdata=False, *args, **kwargs):
    """docstring for fireBaseIO"""
    exacturl = 'https://%s.firebaseio.com/%s.json' % (app, path)
    # if method patch|put|post and data is None raise Error ## TODO
    logging.debug(exacturl)
    if method == 'get':
        jd = json.JSONDecoder().decode
        return requests.get(exacturl).json()
    if method == 'patch':
        if bigdata:
            for k, v in data.iteritems():
                exacturl = 'https://%s.firebaseio.com/%s/%s.json' % (
                    app, path, k)
                requests.patch(exacturl, json.dumps(v))
                print ('Data sent to %s' % exacturl)
            return
        requests.patch(exacturl, json.dumps(data))
    elif method == 'put':
        requests.put(exacturl, json.dumps(data))
    elif method == 'post':
        requests.post(exacturl, json.dumps(data))
    print 'Data sent to %s with %s method' % (exacturl, method)
    return
