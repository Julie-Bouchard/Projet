# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:56:31 2021

@author: Julie
"""

from estimateur import Estimateur

class Moyenne(Estimateur):
    def __init__(self, variable):
        self.variable=variable
    def estime(self):    
        n= len(self.variable.lignes)+1
        moyenne=0
        for i in range (1,n):
            moyenne+=float(self.variable.lignes[i-1][0])
        moyenne= moyenne / (n-1)
        return moyenne
