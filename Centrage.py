# -*- coding: utf-8 -*-
"""
Created on Mon May  3 02:06:01 2021

@author: maroi
"""
import Statistique_descriptive as sd

class Centrage:
    def __init__(self):
        self.centree="False"
        
    def centrer(self):
        n,p = self.shape
        for j in range (0,p):
            U=self[:,[j]] # On selectionne la j ème colonne de notre base de donnée
            moyenne=sd.moyenne(U)
            for i in range (0,n):
                self[i,j]=self[i,j]-moyenne
        self.centree="True"