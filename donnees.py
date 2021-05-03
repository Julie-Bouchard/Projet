# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 12:03:42 2021

@author: Julie
"""

class Donnees:
    def __init__(self,nombre_lignes,nombre_colonnes):
        self.nombre_lignes=nombre_lignes
        self.nombre_colonnes=nombre_colonnes
       
    def donnees(self):
        return [[0]*self.nombre_colonnes for i in range(self.nombre_lignes)]