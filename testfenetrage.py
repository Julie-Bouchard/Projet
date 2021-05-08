# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:38:37 2021

@author: id1776
"""

from datetime import datetime

def convertirdate(datestr):
    #Exemple de datestr : "2020-03-19"
    return datetime.strptime(datestr,"%Y-%m-%d")

def fenetrage(Donnees,debut_periode,fin_periode):
        fenetre=[Donnees[0]]
        d=convertirdate(debut_periode)
        f=convertirdate(fin_periode)
        for j in range(len(Donnees[0])):
            if Donnees[0][j]=="jour":
                for i in range(1,len(Donnees)):
                    if convertirdate(Donnees[i][j])>=d and convertirdate(Donnees[i][j])<=f:
                        fenetre.append(Donnees[i])
        return(fenetre)
        
f=fenetrage(Tableau1,"2020-03-19","2020-03-20")
print(f)

