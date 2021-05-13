# -*- coding: utf-8 -*-
"""
Created on Thu May  6 08:21:33 2021
@author: id1780
"""

from affichage import Affichage
import csv

class Tableau(Affichage):
    
    def __init__(self, emplacement_fichier):
        self.emplacement_fichier = emplacement_fichier

    def affiche(self, table):
        with open(self.emplacement_fichier,'w',newline='') as fichiercsv :
            ecrire = csv.writer(fichiercsv, delimiter=';')
            ecrire.writerow(table.noms_colonnes)
            for ligne in table.lignes :
                ecrire.writerow(ligne)
