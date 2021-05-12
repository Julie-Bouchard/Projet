# -*- coding: utf-8 -*-
"""
Created on Thu May  6 08:21:33 2021

@author: id1780
"""

from affichage import Affichage

class Tableau(Affichage):
    
    def __init__(self):
        self.table = []

    def SauvegarderTableauEstimateur(estimateur, fenetrage):
        self.table = estimateur.estime(fenetrage)
        with open('tableur.csv','w',newline='') as f :
            ecrire=csv.writter(f)
            for i in self.table :
                ecrire.writerow(i)
                print('',end='\n')
                print(longueur du tableau :', len(self.table))
        
    def SauvegarderTableauTransformation(transformation, fenetrage):
        self.table = transformation.transforme(fenetrage)
        with open('tableur.csv','w',newline='') as f :
            ecrire=csv.writter(f)
            for i in self.table :
                ecrire.writerow(i)
                print('',end='\n')
                print(longueur du tableau :', len(self.table))
                
