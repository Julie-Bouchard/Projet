# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:21:46 2021

@author: id1776
"""

from transformation import Transformation

class SelectionVariable(Transformation):
    def __init__(self,nom_variable):
        self.nom_variable=nom_variable
    def selectionvariable(self):
        variable=[]
        for j in len(Donnees[1]):
            if Donnees[1][j]==nom_variable:
                for i in len(Donnees):
                    variable.append([Donnees[i][j]])
        return variable