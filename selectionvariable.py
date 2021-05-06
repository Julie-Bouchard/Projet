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
        for j in range(len(Donnees[0])):
            if Donnees[0][j]==nom_variable:
                for i in range(len(Donnees)):
                    variable.append([Donnees[i][j]])
        return variable
