# -*- coding: utf-8 -*-
"""
Created on Tue May 11 01:07:20 2021

@author: id1776
"""

from estimateur import Estimateur
from variance import Variance

class EcartType(Estimateur):
    #self represente un vecteur
    def __init__(self):
        self.ecart_type=0
    def estime(self):    
        n=len(self)
        self.ecart_type=(self.variance)**(1/2)