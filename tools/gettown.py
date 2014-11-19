#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apiv2 import diyanetApiReq
import logging

logging.basicConfig(filename='_logs/gettown.log', level=logging.INFO)

# TODO Memoize this

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



if __name__ == '__main__':
    pass
