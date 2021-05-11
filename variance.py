# -*- coding: utf-8 -*-
"""
Created on Tue May 11 01:03:51 2021

@author: id1776
"""

from estimateur import Estimateur
from moyenne import Moyenne

class Variance(Estimateur):
    #self represente un vecteur
    def __init__(self):
        self.variance=0
    def estime(self):
        n=len(self)
        for i in range (0,n):
            self.variance+=((self[i][0]-self.moyenne)**2)
        self.variance=self.variance / n