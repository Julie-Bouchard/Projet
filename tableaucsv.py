# -*- coding: utf-8 -*-
"""
Created on Thu May  6 08:21:33 2021
@author: id1780
"""

from affichage import Affichage
import csv

class Tableau(Affichage):
    
    def __init__(self, table):
        self.table = table

    def affiche(self, emplacement_fichier):
        with open(emplacement_fichier,'w',newline='') as fichiercsv :
            ecrire = csv.writer(fichiercsv)
            for ligne in self.table :
                ecrire.writerow(ligne)
        
