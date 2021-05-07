# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:12:59 2021

@author: id1776
"""

from transformation import Transformation

class AgregationSpatiale(Transformation):
    def __init__(self,nom_variable,echelle1,echelle2):
        self.nom_variable=nom_variable
        self.echelle1=echelle1
        self.echelle2=echelle2
    def reg_dep(self):
        res={}
        for i in range(len(Donnees["Academie"])):
            res.append({Code_Dpt:Donnees["Academie"]["Code_Dpt"],Region:Donnees["Academie"]["Region"]})
        return res