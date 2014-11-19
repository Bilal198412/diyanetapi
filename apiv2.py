#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import json
from tools.fetch import json_response, dict_response
from tools.toolkits import filterize
import urllib
import requests


def sehirlerDbJsonReq(countryId=2, check=False):
    data = diyanetApiReq(url='PrayerTime/FillState',
                         qargs={'countryCode': countryId})
    if check:
        newdata = {}
        for k,v in data.iteritems():
            newdata[ k.replace('/','-') ] = v
        return newdata
    return data

def ilcelerDbJsonReq(cityId):
    data = diyanetApiReq(url='PrayerTime/FillCity',
                         qargs={'ItemId': cityId}, )
    return data
def fillState(countryCode=2, *args, **kwargs):
    """docstring for fillState"""
    data = diyanetApiReq(url='PrayerTime/FillState',
                         qargs={'countryCode': countryCode})
    return data


def fillCity(cityId, *args, **kwargs):
    """docstring for fillCity"""
    data = diyanetApiReq(url='PrayerTime/FillCity',
                         qargs={'ItemId': cityId}, )
    return data


def prayerTimes(stateName, name, countryName=2, *args, **kwargs):
    """docstring for prayerTimes"""
    data = diyanetApiReq(url='PrayerTime/PrayerTimesSet',
                         qargs={'countryName': countryName,
                                'stateName': stateName,
                                'name': name},
                         method='post', filter=False, *args, **kwargs)
    return data


def diyanetApiReq(url, qargs, method='get', filter=True, dtype='json'):
    # import ipdb; ipdb.set_trace() # BREAKPOINT
    headers = {'content-type': 'application/json', 'encoding': 'utf-8'}
    base = 'http://www.diyanet.gov.tr/'
    # get or post
    url = base + url
    jsonDecode = json.JSONDecoder().decode
    try:
        if method == 'get':
            conn = requests.get(url, params=qargs, headers=headers)
        elif method == 'post':
            conn= requests.post(url, params=qargs, headers=headers)

        if dtype == 'json':
            if filter:
                return filterize(conn.json())
            else:
                return conn.json()
        elif dtype == 'dict':
            if filter:
                return filterize(jsonDecode(json.dumps(conn.json())))
            else:
                return jsonDecode(json.dumps(conn.json()))
    except:
        # TODO log and raise exception
        pass


if __name__ == '__main__':
    # print prayerTimes( stateName = 504, name = 9197, countryName = 2)
    print prayerTimes(countryName=2,
                      stateName=504,
                      name = 9197)

    # print sehirlerDbJsonReq()
    # print ilcelerDbJsonReq(500)

