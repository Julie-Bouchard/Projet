# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:57:31 2021

@author: id1776
"""

from donnees import Donnees
from transformation import Transformation
from estimateur import Estimateur

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
print(table3.noms_colonnes)

d=AgregationSpatiale_reg_dep(table,'dep')
table4=AgregationSpatiale_reg_dep.transforme(d)
print(table4.lignes)

e=Jointure(table,tablea,'dep')
table5=Jointure.transforme(e)
print(table5.lignes)

tableb=Donnees(table.noms_colonnes,table.lignes[:303])
f=MoyenneGlissante(tableb,"incid_hosp",3)
table6=MoyenneGlissante.transforme(f)
print(table6.lignes)
print(table6.noms_colonnes)

tablec=Donnees(['dep','incid_hosp'],[['1','38'],['2','10'],['3','30']])
print(tablec.noms_colonnes)
print(tablec.lignes)

g=SelectionVariablecsv(tablec,"incid_hosp")
tabled=SelectionVariablecsv.transforme(g)
print(tabled.lignes)
print(tabled.noms_colonnes)
h=Moyenne(tabled)
mean=Moyenne.estime(h)
print(mean)

i=Donnees.ajouter_colonne(tablec,'incid_rea',['15','25','35'],1)
print(i.lignes)
print(i.noms_colonnes)

j=Donnees.ajouter_ligne(tablec,['4','42'], position = 1)
print(j.lignes)
print(j.noms_colonnes)

k=Donnees.enlever_ligne(tablec)
print(k.lignes)
print(k.noms_colonnes)

l=Donnees.enlever_colonne(tablec,position=-1)
print(l.lignes)
print(l.noms_colonnes)
