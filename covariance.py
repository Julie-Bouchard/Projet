# -*- coding: utf-8 -*-
"""
Created on Tue May 11 01:15:03 2021

@author: id1776
"""

from estimateur import Estimateur
from moyenne import Moyenne

class Covariance(Estimateur):
    #self represente un vecteur
    def __init__(self):
        self.moyenne=0
    def estime(self,V):    
        n=len(self)
        for i in range (0, n):
            self.covariance+=((self[i][0]-self.moyenne)*(V[i][0]-V.moyenne))
        self.covariance = self.covariance / n