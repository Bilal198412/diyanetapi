#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import json
from tools.fetch import json_response, dict_response
from tools.toolkits import filterize
from tools.gettown import sehirlerDbJsonReq, ilcelerDbJsonReq
import urllib
import requests


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

# --------- WOULD BE DEPRECATED ---------#


def diyanetApiGet(url, query_args):
    """docstring for diyanetApiGet"""
    baseUrl = 'http://www.diyanet.gov.tr/'
    p = urllib.urlencode(query_args)
    conn = urllib.urlopen(baseUrl + url, p)
    resp = conn.read()
    data = json.JSONDecoder().decode(resp)
    return data


def diyanetApi(url, query_args, dtype='dict', vakit=False, *args, **kwargs):
    """docstring for diyanetapi"""
    baseUrl = 'http://www.diyanet.gov.tr/'
    conn = json_response(baseUrl + url, query_args)

    if dtype == 'dict':
        return dict_response(conn)
    elif dtype == 'json':
        return json.dumps(dict_response(conn))


def vakitCek2(countryName=2, stateName=572, name=9872):
    """docstring for vakitcek"""

    url = 'PrayerTime/PrayerTimesSet'
    query_args = {'countryName': countryName,
                  'itemSource': "inner",
                  'stateName': stateName,
                  'name': name}
    return diyanetApi(url, query_args)


def sehirListe(countryCode=2, *args, **kwargs):
    """docstring for sehirlistesi"""
    url = 'PrayerTime/FillState'
    query_args = {'countryCode': str(countryCode)}
    return diyanetApiGet(url, query_args)


def ilceListe(ItemId=539, *args, **kwargs):
    """docstring for ilcelistesi"""
    url = 'PrayerTime/FillCity'
    query_args = {'ItemId': str(ItemId)}
    return diyanetApiGet(url, query_args)

# --------------------------


def vakitcek(country_name=2, state_name=572, name=9872, dtype='json'):
    """docstring for fetch"""
    url = 'http://www.diyanet.gov.tr/PrayerTime/PrayerTimesSet'
    query_args = {'countryName': country_name,
                  'itemSource': "inner",
                  'stateName': state_name,
                  'name': name}

    conn = json_response(url, query_args)

    if dtype == 'dict':
        return dict_response(conn)
    elif dtype == 'json':
        return json.dumps(dict_response(conn))


if __name__ == '__main__':
    # print vakitCek2()
    # import ipdb; ipdb.set_trace() # BREAKPOINT
    # x = ilceListe()
    # print x
    # print prayerTimes( stateName = 504, name = 9197, countryName = 2)
    print prayerTimes(countryName=2,
                      stateName=504,
                      name = 9197)

    # print sehirlerDbJsonReq()
    print ilcelerDbJsonReq(500)

