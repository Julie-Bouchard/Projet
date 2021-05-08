# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:44:30 2021

@author: id1776
"""

import csv
import json

def chargementcsv(emplacement_fichier):
    data = []
    with open(emplacement_fichier, encoding='ISO-8859-1') as csvfile :
        covidreader = csv.reader(csvfile, delimiter=';')
        for row in covidreader :
            data.append(row)
    return data
        
Tableau1=chargementcsv("P:/ProjetTraitement/Données Hospitalisations Covid-19 en France-20210506/Données/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv")
print(Tableau1)

def chargementjson(emplacement_fichier):
        with open(emplacement_fichier) as json_file :
            data = json.load(json_file)
        return(data)
    
Tableau2=chargementjson("P:/ProjetTraitement/VacancesScolaires.json")
print(Tableau2)
