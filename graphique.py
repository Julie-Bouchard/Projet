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
    
    def __init__(self, titre, abscisse, ordonnee):
        self.titre = titre # de type str, il correspond au titre que l'on veut donner au graphique
        self.abscisse = abscisse # de type str, il correspond au nom de la variable que l'on veut mettre en abscisse sur le graphe
        self.ordonnee = ordonnee # de type str, il correspond au nom de la variable que l'on veut mettre en ordonnee sur le graphe
    
    def affiche(self, table):
        x = [] # liste des abscisses du graphique
        y = [] # liste des ordonnées du graphique
        indice_colonne_x = table.noms_colonnes.index(self.abscisse) # numero de la colonne associee à la variable que l'ont veut en abscisse
        indice_colonne_y = table.noms_colonnes.index(self.ordonnee) # numero de la colonne associee à la variable que l'ont veut en ordonnee
        n = len(table.lignes) 
        for i in range(n) :
            x.append(table.lignes[i][indice_colonne_x])
            y.append(table.lignes[i][indice_colonne_y])
        plt.ylabel(self.ordonnee)
        plt.xlabel(self.abscisse)
        plt.title(self.titre)
        plt.plot(x,y,'b')
        plt.show()
