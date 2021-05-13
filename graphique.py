from affichage import Affichage
import matplotlib.pyplot as plt
import numpy as np

class Graphique(Affichage):
    
    def __init__(self, titre, abscisse, ordonnee, table):
        self.titre = titre
        self.abscisse = abscisse
        self.ordonnee = ordonnee
        self.table = table
    
    def affiche(self):
        n = len(table)
        x = self.table[0]
        y = [self.table[1]]
        plt.ylabel(ordonnee)
        plt.xlabel(abscisse)
        plt.title(titre)
        plt.plot(x,y,'b')
        plt.show()
