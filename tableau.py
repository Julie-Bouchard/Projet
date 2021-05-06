# -*- coding: utf-8 -*-
"""
Created on Thu May  6 08:21:33 2021

@author: id1780
"""

from affichage import Affichage

class Tableau(Affichage):
    
    def __init__(self):
        self.table = []

    def SauvegarderTableauEstimateur(estimateur, fenetrage):
        self.table = estimateur.estime(fenetrage)
        
    def SauvegarderTableauTransformation(transformation, fenetrage):
        self.table = transformation.transforme(fenetrage)
