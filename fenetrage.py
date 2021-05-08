# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:59:57 2021

@author: id1776
"""

from transformation import Transformation
from datetime import datetime

def convertirdate(datestr):
        #Exemple de datestr : "2020-03-19"
        return datetime.strptime(datestr,"%Y-%m-%d")

class Fenetrage(Transformation):
    def __init__(self,debut_periode,fin_periode):
        self.debut_periode=debut_periode
        self.fin_periode=fin_periode
    def fenetrage(self):
        fenetre=[self.Donnees[0]]
        d=convertirdate(self.debut_periode)
        f=convertirdate(self.fin_periode)
        for j in range(len(self.Donnees[0])):
            if self.Donnees[0][j]=="jour":
                for i in range(1,len(self.Donnees)):
                    if convertirdate(self.Donnees[i][j])>=d and convertirdate(self.Donnees[i][j])<=f:
                        fenetre.append(self.Donnees[i])
        return(fenetre)
