# -*- coding: utf-8 -*-
"""
Created on Thu May  6 07:40:06 2021

@author: id1780
"""

from abc import ABC, abstractmethod
from estimateur import Estimateur
from transformation import Transformation

class Affichage(Estimateur, Transformation):
   
    @abstractmethod
    def affiche(self):
        pass
