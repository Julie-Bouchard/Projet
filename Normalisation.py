# -*- coding: utf-8 -*-
"""
Created on Sun May  2 14:20:48 2021

@author: maroi
"""

import Statistique_descriptive as sd

class Normalisation:
    def __init__(self):
        self.normalisee="False"
        
    def normaliser(self):
        n,p = self.shape
        for j in range (0,p):
            U=self[:,[j]] # On selectionne la j ème colonne de notre base de donnée
            ecart_type=sd.ecart_type(U)
            for i in range (0,n):
                self[i,j]=self[i,j]/ecart_type
        self.normalisee="True"
        
        