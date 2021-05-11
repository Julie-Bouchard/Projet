# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:57:31 2021

@author: id1776
"""

from donnees import Donnees
from transformation import Transformation

a=ChargementDeDonneescsv("P:/ProjetTraitement/Données Hospitalisations Covid-19 en France-20210506/Données/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv")
table=ChargementDeDonneescsv.transforme(a)

a2=ChargementDeDonneescsv("P:/ProjetTraitement/Données Hospitalisations Covid-19 en France-20210506/Données/donnees-hospitalieres-covid19-2021-03-03-17h03.csv")
tablea=ChargementDeDonneescsv.transforme(a2)

b=Fenetrage(table,"2020-03-19","2020-03-20")
table2=Fenetrage.transforme(b)
print(table2.lignes)
print(table2.noms_colonnes)

c=SelectionVariablecsv(table,'dep')
table3=SelectionVariablecsv.transforme(c)
print(table3.lignes)

d=AgregationSpatiale_reg_dep(table,'dep')
table4=AgregationSpatiale_reg_dep.transforme(d)
print(table4.lignes)

e=Jointure(table,tablea,'dep')
table5=Jointure.transforme(e)
print(table5.lignes)
