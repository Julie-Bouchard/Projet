# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:43:11 2021

@author: Julie
"""

from transformation import Transformation
import csv

class ChargementDeDonnees(Transformation):
    def __init__(self,emplacement_fichier):
        self.emplacement_fichier=emplacement_fichier
    def chargementdedonnees(self):
        #Exemple d'emplacement_fichier : 'C:/Users/Julie/Documents/1A/Projet de traitement de données/Données Hospitalisations Covid-19 en France-20210503/Données/covid-hospit-incid-reg-2021-03-03-17h20.csv'
        Tableau = []
        #Ouverture et lecture du fichier csv
        f = open(self.emplacement_fichier)
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
