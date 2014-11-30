#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import logging
import json
from tools.toolkits import filterize
import requests
try:
    from google.appengine.api import memcache
except:
    import memcache as memcached
    memcache = memcached.Client(['127.0.0.1:11211'], debug=1)

# xx = '-1261178572836802836'
# logging.debug ( memcache.get(xx) )
# logging.debug ( ' ********************')


def func_hash(*args, **kwargs):

    # TODO improve this by all types so calc hashes with no exception
    # Like getattr(var, 'hash__'
    # TODO check if there is iterable (list|dict) type in args|kwargs

    def hash_args(*args):
        """docstring for main"""
        hlist = []
        for v in sorted(args):
            if hasattr(v, '__iter__'):
                result = {
                    'tuple': lambda: v,
                    'list': lambda: tuple(sorted(v)),
                    'dict': lambda: tuple(sorted(v.items()))
                }[type(v).__name__]()
                hlist.append(result)
            else:
                hlist.append(v)
        return hash(tuple(hlist))

    def hash_kwargs(**kwargs):
        """docstring for main"""
        hlist = []
        for k, v in sorted(kwargs.iteritems()):
            if hasattr(v, '__iter__'):
                result = {
                    'tuple': lambda: v,
                    'list': lambda: tuple(sorted(v)),
                    'dict': lambda: tuple(sorted(v.items()))
                }[type(v).__name__]()
                hlist.append(result)
            else:
                hlist.append((k, v))
        return hash(tuple(hlist))

    return str(hash_kwargs(**kwargs) + hash_args(*args))

# def cache(func):


class cache(object):

    def __init__(self, func):
        self.func = func

        for name in set(dir(func)) - set(dir(self)):
            setattr(self, name, getattr(func, name))

    def __call__(self, *args, **kwargs):
        self.key = func_hash(*args, **kwargs)
        if self.is_cached():
            logging.warning(
                '>>>>> Serving from cache for key :\t %s' % self.key)
            return self.cache_data()
        else:
            # call function to get data
            data = self.func(*args, **kwargs)
            # Put this data to memcache
            memcache.set(self.key, data, time=60 * 60 * 24)
            # Return function
            return self.func(*args, **kwargs)
        return self.func(*args, **kwargs)  # OK

    def is_cached(self):
        data = memcache.get(self.key)
        return data is not None

    def cache_data(self, *args, **kwargs):
        # data = self.func(*args, **kwargs)
        return memcache.get(self.key)


def sehirlerDbJsonReq(countryId=2, check=False):
    data = diyanetApiReq(url='PrayerTime/FillState',
                         qargs={'countryCode': countryId})
    if check:
        newdata = {}
        for k, v in data.iteritems():
            newdata[k.replace('/', '-')] = v
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


@cache
def prayerTimes(*args, **kwargs):
    """
    Parameters
    nid,
    stateName=None,
    countryName=2,
    minimal=True
    """
    json_data = diyanetApiReq(url='PrayerTime/PrayerTimesSet',
                              qargs={'countryName': None,
                                     'stateName': None,
                                     'name': kwargs['nid']},
                              method='post', filter=False, *args, **kwargs)
    # raise Exception | ValueError | requests.exceptino.HTTPError
    if kwargs.get('minimal', True):
        data = {}
        keys = ['HicriTarih', 'UlkeAdi', 'SehirAdi', 'KibleAcisi', 'MoonSrc',
                'Imsak', 'Gunes', 'Ogle', 'Ikindi', 'Aksam', 'Yatsi']
        for k in keys:
            data[k] = json_data[k]
    else:
        data = json_data
    return data


@cache
def diyanetApiReq(url, qargs, method='get', filter=True, *args, **kwargs):
    # import ipdb; ipdb.set_trace() # BREAKPOINT
    headers = {'content-type': 'application/json', 'encoding': 'utf-8'}
    base = 'http://www.diyanet.gov.tr/'
    # get or post
    url = base + url
    # TODO Lots of todo is here
    # Refactor this function, implement dtype = dict|json
    # Switch case
    try:
        if method == 'get':
            data = requests.get(url, params=qargs, headers=headers).json()
        elif method == 'post':
            data = requests.post(url, params=qargs, headers=headers).json()

            if filter:
                return filterize(data)
            else:
                return data
    except:
        # TODO log and raise exception
        pass


if __name__ == '__main__':
    # print prayerTimes(nid = 9955)
    @cache
    def foo(*args, **kwargs):
        return kwargs['nid'] + 1

    print foo(nid=55555)
    # print foo(nid=10000)
    # print foo(nid=10)
    # print foo(nid=100)
    # print foo(nid=100)
