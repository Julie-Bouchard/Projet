# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:59:57 2021

@author: id1776
"""

from transformation import Transformation

class Fenetrage(Transformation):
    def __init__(self,debut_periode,fin_periode):
        self.debut_periode=debut_periode
        self.fin_periode=fin_periode
    def fenetrage(self):
        fenetre=[]
        for j in len(Donnees[1]):
            if Donnees[1][j]=="jour":
                for i in len(Donnees):
                    if Donnees[i][j]==debut_periode:
                        fenetre.append(Donnees[i])
                        k=i
                while Donnees[k][j]!=fin_periode:
                    fenetre.append(Donnees[k])
                    k+=1
                fenetre.append(Donnees[k+1][j])
        return(fenetre)
