# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:56:31 2021

@author: Julie
"""

from estimateur import Estimateur

class Moyenne(Estimateur):
    #self represente un vecteur
    def __init__(self):
        self.moyenne=0
    def estime(self):    
        n= len(self)
        for i in range (0,n):
            self.moyenne+=self[i,0]
        self.moyenne=self.moyenne / n
