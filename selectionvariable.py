# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:21:46 2021

@author: id1776
"""

from transformation import Transformation

class SelectionVariable(Transformation):
    def __init__(self,nom_variable):
        self.nom_variable=nom_variable
        #Exemples nom_variable : "dep","Code_Dpt"
    def selectionvariablecsv(self):
        #Renvoie une liste de listes
        variable=[]
        for j in range(len(self.Donnees[0])):
            if self.Donnees[0][j]==self.nom_variable:
                for i in range(len(self.Donnees)):
                    variable.append([self.Donnees[i][j]])
        return variable
    def selectionvariablejson(self):
        #Renvoie une liste de dictionnaires
        variable=[]
        if self.Donnees["Calendrier"][0].has_key(self.nom_variable):
            for i in range(len(self.Donnees["Calendrier"])):
                variable.append({self.nom_variable:self.Donnees["Calendrier"][i][self.nom_variable]})
        elif self.Donnees["Academie"][0].has_key(self.nom_variable):
            for i in range(len(self.Donnees["Academie"])):
                variable.append({self.nom_variable:self.Donnees["Academie"][i][self.nom_variable]})
        return variable
