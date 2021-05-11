# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:59:57 2021

@author: id1776
"""

from transformation import Transformation
from donnees import Donnees
from datetime import datetime

def convertirdate(datestr):
        #Exemple de datestr : "2020-03-19"
        return datetime.strptime(datestr,"%Y-%m-%d")

class Fenetrage(Transformation):
    def __init__(self,table,debut_periode,fin_periode):
        self.debut_periode=debut_periode
        self.fin_periode=fin_periode
        self.table=table
    def transforme(self):
        fenetre=[self.table.noms_colonnes]
        d=convertirdate(self.debut_periode)
        f=convertirdate(self.fin_periode)
        for j in range(len(self.table.noms_colonnes)):
            if self.table.noms_colonnes[j]=="jour":
                for i in range(1,len(self.table.lignes)+1):
                    if convertirdate(self.table.lignes[i-1][j])>=d and convertirdate(self.table.lignes[i-1][j])<=f:
                        fenetre.append(self.table.lignes[i-1])
        data=Donnees(fenetre[0],fenetre[1:])
        return(data)
