# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:44:30 2021

@author: id1776
"""

import csv

def chargementdedonnees(emplacement_fichier):
        #Exemple d'emplacement_fichier : 'C:/Users/Julie/Documents/1A/Projet de traitement de données/Données Hospitalisations Covid-19 en France-20210503/Données/covid-hospit-incid-reg-2021-03-03-17h20.csv'
        Tableau = []
        #Ouverture et lecture du fichier csv
        f = open(emplacement_fichier)
        csv_f = csv.reader(f)
        for row in csv_f:
            Tableau.append(row)
        f.close
        #Mise en forme du tableau : liste de listes de chaines de caractères
        for i in range(len(Tableau)):
            Tableau[i]=' '.join(Tableau[i])
        Tableau_res=[]
        for i in range(len(Tableau)):
            t=Tableau[i].split(";")
            Tableau_res.append(t)
        return (Tableau_res)
        
Tableau1=chargementdedonnees("P:/ProjetTraitement/Données Hospitalisations Covid-19 en France-20210506/Données/covid-hospit-incid-reg-2021-03-03-17h20.csv")
print(Tableau1)