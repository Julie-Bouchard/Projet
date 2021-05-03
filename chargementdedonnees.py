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
        with open(self.emplacement_fichier, newline='') as csvfile:
            fichier = csv.reader(csvfile, delimiter=' ', quotechar='|')
            print(fichier)