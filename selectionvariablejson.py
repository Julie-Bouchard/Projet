# -*- coding: utf-8 -*-
"""
Created on Mon May 10 17:14:09 2021

@author: id1776
"""

from transformation import Transformation

class SelectionVariablejson(Transformation):
    def __init__(self,fichierjson,nom_variable):
        self.nom_variable=nom_variable
        self.fichierjson=fichierjson
        #Exemples nom_variable : "dep","Code_Dpt"
    def transforme(self):
        #Renvoie une liste de dictionnaires
        variable=[]
        if self.fichierjson["Calendrier"][0].has_key(self.nom_variable):
            for i in range(len(self.fichierjson["Calendrier"])):
                variable.append({self.nom_variable:self.fichierjson["Calendrier"][i][self.nom_variable]})
        elif self.fichierjson["Academie"][0].has_key(self.nom_variable):
            for i in range(len(self.fichierjson["Academie"])):
                variable.append({self.nom_variable:self.fichierjson["Academie"][i][self.nom_variable]})
        return variable