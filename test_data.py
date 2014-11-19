#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

dict = {
    'Imsak': "05:27", 'Gunes': "06:48", 'Ogle': "12:20",
    'Ikindi': "15:17", 'Aksam': "17:40", 'Yatsi': "18:51",
    'NextImsak': None, 'MoonSrc': "/UserFiles/AyEvreleri/r3.gif",
    'HicriTarih': "3 SAFER 1435", 'MiladiTarih': "06 Aralık 2013",
    'RumiTarih': "06 Aralık 1429", 'GunesText': "Güneş vaktine kalan süre",
    'ImsakText': "İmsak vaktine kalan süre", 'OgleText': "Öğle vaktine kalan süre",
    'IkindiText': "İkindi vaktine kalan süre", 'AksamText': "Akşam vaktine kalan süre",
    'YatsiText': "Yatsı vaktine kalan süre",
    'Enlem': 24.46, 'Boylam': 39.62, 'KibleAcisi': 173,
    'UlkeAdi': "SUUDI ARABISTAN", 'SehirAdi': "MEDINE",
    'KibleSaati': "12:01", 'GunesBatis': "17:33", 'GunesDogus': "06:52",
    'HolyDaysItem': None
}

json = json.dumps ( dict )
