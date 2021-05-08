# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:43:11 2021

@author: Julie
"""

from transformation import Transformation
import csv
import json

class ChargementDeDonnees(Transformation):
    def __init__(self,emplacement_fichier):
        self.emplacement_fichier=emplacement_fichier
        #Exemple d'emplacement_fichier : "P:/ProjetTraitement/Données Hospitalisations Covid-19 en France-20210506/Données/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv"
    def chargementcsv(self):
        data = []
        with open(self, encoding='ISO-8859-1') as csvfile :
            covidreader = csv.reader(csvfile, delimiter=';')
            for row in covidreader :
                data.append(row)
        return data
    def chargementjson(self):
        with open(self) as json_file :
            data = json.load(json_file)
        return data
