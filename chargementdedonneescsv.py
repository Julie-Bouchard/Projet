# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:53:08 2021

@author: id1776
"""

from transformation import Transformation
from donnees import Donnees
import csv

class ChargementDeDonneescsv(Transformation):
    def __init__(self,emplacement_fichier):
        self.emplacement_fichier=emplacement_fichier
        #Exemple d'emplacement_fichier : "P:/ProjetTraitement/Données Hospitalisations Covid-19 en France-20210506/Données/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv"
    def transforme(self):
        data = []
        with open(self.emplacement_fichier, encoding='ISO-8859-1') as csvfile :
            covidreader = csv.reader(csvfile, delimiter=';')
            for row in covidreader :
                data.append(row)
        data2 = Donnees(data[0],data[1:])
        return data2