#!/usr/bin/python
# -*- encoding utf-8 -*-
import urllib2
import json
from urllib import urlencode
from time import sleep  # BE A GOOD CITIZEN :)
import logging


def filterVakit(data):
    FILTERED = {}
    FILTRE = ['HicriTarih', 'UlkeAdi', 'SehirAdi', 'KibleAcisi', 'MoonSrc',
              'Imsak', 'Gunes', 'Ogle', 'Ikindi', 'Aksam', 'Yatsi']
    for k in FILTRE:
        FILTERED[k] = data[k]
    return FILTERED  # MINIMAL


def fetchJsonResponse(url, query_args):
    # TODO sleep here
    qdata = urlencode(query_args)

    while True:
        try:
            request = urllib2.Request(url, qdata)
            response = urllib2.urlopen(request)
            break
        except:
            logging.error('### FETCH ERROR WAITING 3.0 s... ###')
            sleep(3.0)
            request = urllib2.Request(url, qdata)
            response = urllib2.urlopen(request)

    respData = response.read()
    data = json.loads(respData)
    return data


def vakitCek(countryName=2, stateName=572, name=9872):
    url = 'http://www.diyanet.gov.tr/PrayerTime/PrayerTimesSet'
    wait = 5.0

    query_args = {'countryName': countryName,
                  'itemSource': "inner",
                  'stateName': stateName,
                  'name': name }
                  # 'name': city.encode('utf-8')}
    while True:
        try:
            jsonResp = fetchJsonResponse(url=url, query_args=query_args)
            break
        except:
            sleep(wait)
            jsonResp = fetchJsonResponse(url=url, query_args=query_args)
    data = filterVakit(jsonResp)
    return data


def fakeNamazVakitleri():

    data = {
        'Imsak': "05:27",
        'Gunes': "06:48",
        'Ogle': "12:20",
        'Ikindi': "15:17",
        'Aksam': "17:40",
        'Yatsi': "18:51",
        'NextImsak': None,
        'MoonSrc': "/UserFiles/AyEvreleri/r3.gif",
        'HicriTarih': "3 SAFER 1435",
        'MiladiTarih': "06 Aralık 2013",
        'RumiTarih': "06 Aralık 1429",
        'GunesText': "Güneş vaktine kalan süre",
        'ImsakText': "İmsak vaktine kalan süre",
        'OgleText': "Öğle vaktine kalan süre",
        'IkindiText': "İkindi vaktine kalan süre",
        'AksamText': "Akşam vaktine kalan süre",
        'YatsiText': "Yatsı vaktine kalan süre",
        'Enlem': 24.46,
        'Boylam': 39.62,
        'KibleAcisi': 173,
        'UlkeAdi': "SUUDI ARABISTAN",
        'SehirAdi': "MEDINE",
        'KibleSaati': "12:01",
        'GunesBatis': "17:33",
        'GunesDogus': "06:52",
        'HolyDaysItem': None
    }

    uns = ['MiladiTarih', 'RumiTarih',
           'GunesText', 'ImsakText', 'OgleText', 'IkindiText', 'AksamText', 'YatsiText']

    for asc in uns:
        data[asc] = data[asc].decode('utf-8')

    vakit = {}
    namazlar = ['HicriTarih', 'UlkeAdi', 'SehirAdi', 'KibleAcisi', 'MoonSrc',
                'Imsak', 'Gunes', 'Ogle', 'Ikindi', 'Aksam', 'Yatsi']
    for k in namazlar:
        vakit[k] = data[k]
    #jsonData =json.loads( data )
    return vakit
