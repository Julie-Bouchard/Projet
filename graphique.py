# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:52:00 2021

@author: id1780
"""

from affichage import Affichage
from transformation import Transformation
import matplotlib.pyplot as plt
import numpy as np

class Graphique(Affichage):
    
    def __init__(self, titre, abscisse, ordonnee, table):
        self.titre = titre
        self.abscisse = abscisse
        self.ordonnee = ordonnee
        self.table = table
    
    def affiche(self):
        x = []
        y = []
        indice_colonne_x = self.table.noms_colonnes.index(self.abscisse)
        indice_colonne_y = self.table.noms_colonnes.index(self.ordonnee)
        n = len(self.table.lignes) 
        for i in range(n) :
            x.append(self.table.lignes[i][indice_colonne_x])
            y.append(self.table.lignes[i][indice_colonne_y])
        plt.ylabel(self.ordonnee)
        plt.xlabel(self.abscisse)
        plt.title(self.titre)
        plt.plot(x,y,'b')
        plt.show()
