#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from tools.firebase import fireBaseIO
from ulkedbv2 import ulkeDict
import logging
import ulkedbv2
from apiv2 import prayerTimes
from tools.gettown import sehirlerDbJsonReq, ilcelerDbJsonReq


def bb():
    ulkeler = ulkeDict(keys=[52, 33])
    ulkeler = ulkeDict(keys=[21, 23, 207, 35, 60, 61,
                             117, 204, 49, 208])
    # ulkeler = ulkeDict(keys=[13])
    # FRANSA, ISPANYA, VUNATU, RUSYA, ABD, AVUSTURYA, MOGOLISTAN, BELCIKA,
    # ALMANYA, INGILTERE, ENDONEZYA,
    for ulke in ulkeler:
        respStates = sehirlerDbJsonReq(ulke, True)
        ulkeler[ulke]['Childs'] = respStates  # sehirlerDbJsonReq( ulke )
        fireBaseIO(app='ahmedseref', path=ulke + '/Childs',
                   data=respStates, bigdata=True)
        # fireBaseIO(app='ahmedseref', path='_TESTS/',
        # data=respStates, method = 'patch',bigdata=True)

        if ulke in ['52', '2', '33']:
            for sehir in ulkeler[ulke]['Childs']:
                packed = ulkeler[ulke]['Childs'][sehir]
                _text, _value = packed['Text'], packed['Value']
                resp = ilcelerDbJsonReq(_value)
                fireBaseIO(app='ahmedseref',
                           path=ulke + '/Childs/' + _text + '/Childs',
                           data=resp)
                # ulkeler[ulke]['Childs'][_text] = resp

    return


def updatePrayerTimes(*args, **kwargs):
    """docstring for updatePrayerTimes"""
    source = dict(countryName='1', stateName=15156, name=15156)
    # TODO Generate a list that contains all state/country/city codes and names
    # Iterate this list

    vakitler = prayerTimes(**source)
    data = dict(Updated={'.sv': 'timestamp'}, Data=vakitler)
    fireBaseIO(source['countryName'] + '/Childs/DIPKARPAZ/Vakitler', data)
    return


def bubi():
    bulky = dict()
    # ulkeler = ulkedbv2.ulkeDict().keys()[190:]
    ulkeler = ulkedbv2.ulkeDict(keys=[21, 23, 207, 35, 60, 61,
                                      13, 15, 117, 204, 49, 146, 208])
    ulkeler = ['13']
    for ulke in ulkeler:
        ukey = str(ulke)
        print ' > Trying %s ' % ulke
        bulky[ukey] = dict()
        db = requests.get(
            'https://ahmedseref.firebaseio.com/%s.json' % ulke).json()
        if int(ulke) not in [52, 2, 33]:
            for i in db['Childs']:
                if not db['Childs'][i].has_key('Value'):
                    print i
                stateName = db['Childs'][i]['Value']
                name = db['Childs'][i]['Value']
                cityData = dict(countryName=ulke,
                                stateName=stateName,
                                name=name,
                                text=i)
                bulky[ukey][stateName] = cityData
        else:
            db = req.get('https://ahmedseref.firebaseio.com/%s/Childs.json' %
                         ulke).json()
            for city in db.keys():  # [u'TEKİRDAĞ']: #db.keys():
                city = city.encode('utf-8').decode('utf-8')
                stateName = db[city]['Value']
                cityData = dict()
                try:
                    for town in db[city]['Childs']:
                        townValue = db[city]['Childs'][town]['Value']
                        townText = db[city]['Childs'][town]['Text']
                        if townText == city:
                            townText = '%s' % city
                        else:
                            townText = '%s/%s' % (city, townText)
                        cityData[townValue] = dict(text=townText,
                                                   countryName=ulke,
                                                   stateName=stateName,
                                                   name=townValue)
                    bulky[ukey][stateName] = cityData
                except:
                    print '----- ERROR ---- in %s' % city  # TEKİRDAĞ
                    pass
        fireBaseIO(
            app='namazvaktim', path=ulke, data=bulky[ulke], bigdata=True)
        print '%s \t OK' % ulke
    # data2json(bulky, 'bulky')
    # fireBaseIO(app = 'namazvaktim' path ='', data = bulky )
    return
if __name__ == '__main__':
    pass
