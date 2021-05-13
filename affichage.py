# -*- coding: utf-8 -*-
"""
Created on Thu May  6 07:40:06 2021

@author: id1780
"""

from abc import ABC, abstractmethod
from donnees import Donnees

class Affichage(Donnees, ABC):
   
    @abstractmethod
    def affiche(self, table):
        pass

