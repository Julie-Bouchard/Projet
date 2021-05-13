# -*- coding: utf-8 -*-
"""
Created on Thu May  6 07:40:06 2021

@author: id1780
"""

from abc import ABC, abstractmethod
from operation import Operation
from transformation import Transformation

class Affichage(Operation, Transformation):
   
    @abstractmethod
    def affiche(self):
        pass
