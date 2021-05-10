# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:57:31 2021

@author: id1776
"""

from donnees1 import Donnees
from chargementdedonnees import ChargementDeDonnees

a=ChargementDeDonnees("P:/ProjetTraitement/Données Hospitalisations Covid-19 en France-20210506/Données/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv")
table=ChargementDeDonnees.chargementcsv(a)
print(table.lignes)