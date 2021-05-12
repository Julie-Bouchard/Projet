# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:21:46 2021

@author: id1776
"""

from transformation import Transformation
from donnees import Donnees

class SelectionVariablecsv(Transformation):
    def __init__(self,table,nom_variable):
        self.nom_variable=nom_variable
        self.table=table
        #Exemples nom_variable : "dep","Code_Dpt"
    def transforme(self):
        #Renvoie une liste de listes
        variable=[[self.nom_variable]]
        for j in range(len(self.table.noms_colonnes)):
            if self.table.noms_colonnes[j]==self.nom_variable:
                for i in range(1,len(self.table.lignes)+1):
                    variable.append([self.table.lignes[i-1][j]])
        data=Donnees(variable[0],variable[1:])
        return data
